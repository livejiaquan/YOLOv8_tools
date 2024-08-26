import os

def remove_class_labels(labels_dir, class_num):
    """
    Remove lines from label files in the specified directory that contain a specified class number.

    Args:
    - labels_dir (str): Path to the directory containing label files.
    - class_num (int): The class number to remove from the label files.
    """
    # Traverse all files in the label directory
    for filename in os.listdir(labels_dir):
        if filename.endswith('.txt'):
            # Read the contents of the label file
            label_path = os.path.join(labels_dir, filename)
            with open(label_path, 'r') as f:
                lines = f.readlines()

            # Remove lines containing the specified class number
            modified_lines = []
            for line in lines:
                class_id, *rest = line.strip().split()
                if int(class_id) != class_num:
                    modified_lines.append(line)

            # Write the modified label file
            with open(label_path, 'w') as f:
                f.writelines(modified_lines)

            print(f"Removed class {class_num} labels from file: {filename}")

def run():
    """
    Run function to execute the removal of specified class labels process.
    """
    print("\n------ Remove Class Labels Tool ------\n")
    labels_dir = input("Enter the path to the labels directory: ").strip()
    class_num = int(input("Enter the class number to remove: ").strip())

    remove_class_labels(labels_dir, class_num)
    print(f"Removed class {class_num} labels from all label files in directory: {labels_dir}")

if __name__ == "__main__":
    
    run()
