import os

def find_files_with_only_target_class(labels_dir, target_class):
    """
    Traverse all label files in the given directory and print files that contain only the target class.

    Parameters:
    labels_dir (str): The directory where the YOLO label files are located.
    target_class (str): The target class to look for in the label files.
    """
    for filename in os.listdir(labels_dir):
        if filename.endswith('.txt'):
            label_path = os.path.join(labels_dir, filename)
            with open(label_path, 'r') as f:
                lines = f.readlines()
            
            # Check if the file contains only the target class
            contains_only_target_class = all(line.split()[0] == target_class for line in lines)
            
            if contains_only_target_class:
                print(f"File name: {filename}")

def get_labels_dir(dataset_dir):
    """
    Determine the correct labels directory based on user input.

    Parameters:
    dataset_dir (str): The directory path provided by the user.

    Returns:
    str: The path to the labels directory if found, otherwise None.
    """
    if os.path.isdir(os.path.join(dataset_dir, 'labels')):
        return os.path.join(dataset_dir, 'labels')
    elif os.path.basename(dataset_dir) == 'labels' and os.path.isdir(dataset_dir):
        return dataset_dir
    else:
        return None

def run():
    """
    Main function to run the process of finding files with only the target class.
    It asks for user input for the dataset directory and the target class.
    """
    print("\n------ YOLO Dataset find target class files ------\n")
    dataset_dir = input("Enter the path to the dataset root folder: ").strip()
    target_class = input("Please enter the target class (e.g., '2'): ").strip()

    labels_dir = get_labels_dir(dataset_dir)

    if labels_dir is not None:
        find_files_with_only_target_class(labels_dir, target_class)
    else:
        print("Error: Could not find 'labels' directory in the specified path.")

if __name__ == "__main__":
    run()
