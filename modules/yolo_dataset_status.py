import os
from collections import Counter
import yaml

def count_images_and_labels(source_path):
    """
    Count the number of images and labels in the dataset.

    Parameters:
    source_path (str): The root directory path where the dataset is located.
    
    Returns:
    tuple: A tuple containing the number of images and the number of labels.
    """
    image_count = 0
    label_count = 0

    for root, dirs, files in os.walk(source_path):
        if 'images' in dirs:
            images_path = os.path.join(root, 'images')
            for image_file in os.listdir(images_path):
                if image_file.endswith(('.jpg', '.png', '.jpeg')):
                    image_count += 1
        
        if 'labels' in dirs:
            labels_path = os.path.join(root, 'labels')
            for label_file in os.listdir(labels_path):
                if label_file.endswith('.txt'):
                    label_count += 1

    return image_count, label_count

def count_class_ids_and_boxes(source_path):
    """
    Traverse all label files under the source_path directory, count the number of each class id,
    count the total number of labeled boxes, and check for lines that do not conform to the labeling format.

    Parameters:
    source_path (str): The root directory path where the label files are located.
    
    Returns:
    tuple: A tuple containing a counter for each class id and its quantity, the total number of labeled boxes,
           and the number of lines that do not conform to the format along with the corresponding file.
    """
    class_id_count = Counter()
    total_boxes = 0
    invalid_lines = []

    for root, dirs, files in os.walk(source_path):
        if 'labels' in dirs:
            labels_path = os.path.join(root, 'labels')
            for label_file in os.listdir(labels_path):
                if label_file.endswith('.txt'):
                    with open(os.path.join(labels_path, label_file), 'r') as f:
                        lines = f.readlines()
                        for line_num, line in enumerate(lines, start=1):
                            total_boxes += 1
                            parts = line.split()
                            if len(parts) > 0 and parts[0].isdigit():
                                class_id = int(parts[0])
                                class_id_count[class_id] += 1
                            else:
                                invalid_lines.append((os.path.join(labels_path, label_file), line_num, line.strip()))

    return class_id_count, total_boxes, invalid_lines

def read_data_yaml(source_path):
    """
    Read the content of the data.yaml file if it exists and ensure only one data.yaml file is present.

    Parameters:
    source_path (str): The root directory path where the dataset is located.
    
    Returns:
    dict: A dictionary containing the content of data.yaml file.

    Raises:
    FileNotFoundError: If no data.yaml file is found.
    ValueError: If multiple data.yaml files are found.
    """
    data_yaml_content = {}
    yaml_files = []

    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file == 'data.yaml':
                yaml_files.append(os.path.join(root, file))

    if len(yaml_files) == 0:
        raise FileNotFoundError("No data.yaml file found.")
    elif len(yaml_files) > 1:
        raise ValueError("Multiple data.yaml files found. Only one data.yaml file should be present.")
    
    with open(yaml_files[0], 'r') as f:
        data_yaml_content = yaml.safe_load(f)
    
    return data_yaml_content

def fix_invalid_lines(invalid_lines):
    """
    Fix lines that do not conform to the labeling format by converting invalid class id data to integers.

    Parameters:
    invalid_lines (list): A list of tuples containing lines that do not conform to the format,
                          each tuple contains the file path, line number, and line content.
    """
    for file, line_num, line in invalid_lines:
        parts = line.split()
        try:
            parts[0] = str(int(float(parts[0])))
            new_line = " ".join(parts) + "\n"
            
            with open(file, 'r') as f:
                lines = f.readlines()
            
            lines[line_num - 1] = new_line
            
            with open(file, 'w') as f:
                f.writelines(lines)
            
            print(f"Fixed file: {file}, line number: {line_num}, content: {new_line.strip()}")
        except ValueError:
            print(f"Unable to fix file: {file}, line number: {line_num}, content: {line.strip()}")
def run():
    print("\n------ YOLO Dataset status ------\n")
    source_path = input("Enter the path to the dataset root folder: ").strip()
    
    image_count, label_count = count_images_and_labels(source_path)
    class_id_counts, total_boxes, invalid_lines = count_class_ids_and_boxes(source_path)
    
    print(f"Total images: {image_count}")
    print(f"Total labels: {label_count}")
    print(f"Total Bounding boxes: {total_boxes}")
    
    for class_id in sorted(class_id_counts):
        print(f"Class ID {class_id}: {class_id_counts[class_id]} instances")
    
    print(f"Number of lines that do not conform to the format: {len(invalid_lines)}")
    if invalid_lines:
        print("Lines that do not conform to the format:")
        for file, line_num, line in invalid_lines:
            print(f"File: {file}, line number: {line_num}, content: {line}")
        
        fix_choice = input("Do you want to automatically fix the lines that do not conform to the format? (y/n): ").strip().lower()
        if fix_choice == 'y':
            fix_invalid_lines(invalid_lines)
            print("Fix completed.")
        else:
            print("No fix performed.")

    yaml_choice = input("Do you want to read the data.yaml file? (y/n): ").strip().lower()
    if yaml_choice == 'y':
        try:
            data_yaml_content = read_data_yaml(source_path)
            print("\ndata.yaml content:")
            print(yaml.dump(data_yaml_content, default_flow_style=False))
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    
    run()