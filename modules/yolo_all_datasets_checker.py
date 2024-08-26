from collections import Counter
import os
import yaml
import pandas as pd
from datetime import datetime

def load_class_names(source_path):
    """
    Traverse the subdirectories under source_path, read the data.yaml file in each subdirectory,
    and extract the class names and comments from it.

    Args:
    - source_path (str): Root directory path of the dataset.

    Returns:
    dict: A dictionary where each subdirectory path relative to source_path is a key,
          and the value is a dictionary containing class names and comments extracted from the data.yaml file.
    """
    class_names_dict = {}

    for root, _, _ in os.walk(source_path):
        class_names_file = os.path.join(root, 'data.yaml')
        if os.path.exists(class_names_file):
            with open(class_names_file, 'r') as f:
                class_names_data = yaml.safe_load(f)
                class_names_dict[os.path.relpath(root, source_path)] = {
                    'names': class_names_data.get('names', {}),
                    'comments': class_names_data.get('comments', '')
                }

    return class_names_dict

def count_boxes_by_class(labels_path, class_names):
    """
    Count the number of bounding boxes for each class in the labels_path directory and check if specific classes exist.

    Args:
    - labels_path (str): Directory path containing label files.
    - class_names (dict): Dictionary containing class IDs and class names.

    Returns:
    Counter: A counter containing the count of bounding boxes for each class name and a flag indicating if specific classes exist.
    """
    boxes_count = Counter()
    yaml_class_names = {}
    total_boxes = 0  # Initialize total boxes counter

    # Get parent directory path
    parent_dir = os.path.dirname(labels_path)
    # Construct path to data.yaml file in parent directory
    data_yaml_path = os.path.join(parent_dir, 'data.yaml')

    if os.path.exists(data_yaml_path):
        with open(data_yaml_path, 'r') as f:
            data = yaml.safe_load(f)
            # Read class names from data.yaml file
            yaml_class_names = data.get('names', {})

    # Traverse label files
    error_logged = False
    for label_file in os.listdir(labels_path):
        if label_file.endswith('.txt'):
            with open(os.path.join(labels_path, label_file), 'r') as f:
                lines = f.readlines()
                total_boxes += len(lines)  # Count total bounding boxes
                for line in lines:
                    try:
                        class_id = int(line.split()[0])
                        if class_id in class_names['names']:
                            class_name = class_names['names'][class_id]
                            boxes_count[class_name] += 1
                    except ValueError:
                        if not error_logged:
                            print(f"{os.path.basename(parent_dir)}: ")
                        error_logged = True
                        print(f"Invalid line in {label_file}: {line.strip()}. Skipping this line...")

    # Check if classes exist
    for class_id, class_name in class_names['names'].items():
        check_name = f"c_{class_name}"
        boxes_count[check_name] = class_id in yaml_class_names

    boxes_count['total_boxes'] = total_boxes  # Add total boxes counter to results
    
    return boxes_count

def check_status(images_files, labels_files, total_boxes, all_class_names):
    # Initialize status as "OK"
    status = "OK"
    all_checks_passed = True  # Track if all checks passed

    # Check if number of image files matches number of label files
    if len(images_files) != len(labels_files):
        status = f"Missing {abs(len(images_files) - len(labels_files))} files"
        all_checks_passed = False

    # Calculate sum of bounding boxes for all classes not starting with 'c_'
    calculated_total_boxes = sum(total_boxes[name] for name in all_class_names)
    
    # Check if total_boxes count matches calculated bounding boxes count
    if total_boxes['total_boxes'] != calculated_total_boxes:
        if all_checks_passed:
            status = f"{total_boxes['total_boxes'] - calculated_total_boxes} Box Nomatch"
        else:
            status += f", {total_boxes['total_boxes'] - calculated_total_boxes} Box Nomatch"
        all_checks_passed = False

    # Return "OK" if all checks passed
    if all_checks_passed:
        return "OK"
    
    return status

def check_dataset(source_path, output_excel=False):
    """
    Check the dataset under source_path, count the number of image and label files in each directory,
    count the number of bounding boxes for each class, and output the results to the console and optionally to a CSV file.

    Args:
    - source_path (str): Root directory path of the dataset.
    - output_excel (bool): Whether to output the results to a CSV file, default is False.

    Returns:
    None
    """
    # Load class names and comments
    class_names_dict = load_class_names(source_path)
    all_class_names = set(item for sublist in class_names_dict.values() for item in sublist['names'].values())

    # Initialize a DataFrame to store the results
    columns = ['Folder', 'Images', 'Boxes']
    for name in sorted(all_class_names):
        columns.append(f' ')
        columns.append(name)
    columns.append('Status')
    columns.append('Comments')
    df = pd.DataFrame(columns=columns)

    print("Checking YOLO Datasets...")

    # Recursively traverse source_path
    for root, dirs, _ in os.walk(source_path):
        if 'images' in dirs and 'labels' in dirs:
            images_path = os.path.join(root, 'images')
            labels_path = os.path.join(root, 'labels')

            images_files = [f for f in os.listdir(images_path) if f.endswith('.jpg') or f.endswith('.png')]
            labels_files = [f for f in os.listdir(labels_path) if f.endswith('.txt')]

            # Get class names and comments for the current directory
            class_names_data = class_names_dict.get(os.path.relpath(root, source_path), {'names': {}, 'comments': 'No data.yaml file found'})
            
            # Count bounding boxes for each class
            total_boxes = count_boxes_by_class(labels_path, class_names_data)
            
            status = check_status(images_files, labels_files, total_boxes, all_class_names)

            row_data = [os.path.relpath(root, source_path), len(images_files), total_boxes['total_boxes']]

            for name in sorted(all_class_names):
                row_data.append('V' if total_boxes[f'c_{name}'] else 'O')
                row_data.append(total_boxes[name] if name in total_boxes else 0)

            row_data.append(status)
            row_data.append(class_names_data['comments'])

            # Add data to DataFrame
            df.loc[len(df)] = row_data

    # Print DataFrame to console
    print(df.to_string(index=False))

    # Output results to a CSV file if requested
    if output_excel:
        now = datetime.now()
        formatted_date_time = now.strftime("%Y%m%d_%H%M")
        excel_path = os.path.join(source_path, formatted_date_time + '_YOLO_dataset_check.csv')
        if os.path.exists(excel_path):
            os.remove(excel_path)
        df.to_csv(excel_path, index=False)

def run():
    """
    Run function to execute the check_dataset function.
    """
    print("\n------ YOLO Dataset Checker ------\n")
    source = input("Enter the path to the main folder containing the datasets: ").strip()
    output_excel = input("Do you want to output the results to a CSV file? (y/n): ").strip().lower() == 'y'
    check_dataset(source, output_excel)

if __name__ == "__main__":
    
    run()
