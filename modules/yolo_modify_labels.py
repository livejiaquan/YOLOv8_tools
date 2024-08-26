import os

def modify_labels(labels_dir, class_id_mapping):
    """
    Replace specified classes in YOLO label files with other classes according to the provided mapping.

    Args:
    - labels_dir (str): Directory path containing label files.
    - class_id_mapping (dict): Dictionary mapping original class IDs to new class IDs.
    """
    # Ensure the labels_dir path ends with a separator
    if not labels_dir.endswith(os.sep):
        labels_dir += os.sep

    # Check if labels_dir exists
    if not os.path.exists(labels_dir):
        print(f"Error: The specified directory '{labels_dir}' does not exist.")
        return

    # Check for 'labels' subdirectory inside labels_dir
    labels_subdir = os.path.join(labels_dir, 'labels')
    if os.path.exists(labels_subdir) and os.path.isdir(labels_subdir):
        labels_dir = labels_subdir
    else:
        print(f"Error: The 'labels' directory does not exist inside '{labels_dir}'.")
        return

    # Traverse labels directory
    for filename in os.listdir(labels_dir):
        if filename.endswith('.txt'):
            # Read content of label file
            label_path = os.path.join(labels_dir, filename)
            with open(label_path, 'r') as f:
                lines = f.readlines()

            # Modify class IDs
            modified_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    class_id = parts[0]
                    if int(class_id) in class_id_mapping:
                        new_class_id = class_id_mapping[int(class_id)]
                        modified_line = f"{new_class_id} {' '.join(parts[1:])}\n"
                        modified_lines.append(modified_line)
                    else:
                        modified_lines.append(line)

            # Write modified label file
            with open(label_path, 'w') as f:
                f.writelines(modified_lines)

    print("Label files modified.")

def run():
    print("\n------ YOLO Label Class ID Modifier ------\n")
    print("You can edit the 'class_id_mapping' dictionary in the script.")
    # Custom class ID mapping
    class_id_mapping = {
        # Example mappings:
        7: 1,  # Replace '0' class with '2' class
        # 1: 3,  # Replace '1' class with '3' class
    }

    # Print current class ID mapping for user reference
    if class_id_mapping:
        print("- class_id_mapping:")
        for original_id, new_id in class_id_mapping.items():
            print(f"    {original_id} -> {new_id}")
    else:
        print("- No custom mappings defined yet.")

    # Dataset root directory path
    dataset_dir = input("\nEnter the path to the dataset root folder: ").strip()

    # Ensure the dataset_dir path ends with a separator
    if not dataset_dir.endswith(os.sep):
        dataset_dir += os.sep

    labels_dir = dataset_dir

    # Check if labels directory exists
    if not os.path.exists(labels_dir):
        print(f"Error: The specified directory '{labels_dir}' does not exist.")
        return

    modify_labels(labels_dir, class_id_mapping)


if __name__ == "__main__":
    run()
