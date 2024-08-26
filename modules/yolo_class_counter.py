from pathlib import Path

def count_yolo_classes(labels_dir):
    """
    Count the number of bounding boxes for each class in YOLO label files.

    Args:
    - labels_dir (Path): Directory path containing label files.
    """
    # Initialize class counters
    class_counts = {}

    # Traverse label files in the specified directory
    for label_file in labels_dir.glob("*.txt"):
        with open(label_file, "r") as f:
            lines = f.readlines()
            # Iterate through each annotation box
            for line in lines:
                class_id = int(line.split()[0])  # Get class ID of the box
                # Increase the corresponding class counter
                if class_id in class_counts:
                    class_counts[class_id] += 1
                else:
                    class_counts[class_id] = 1

    # Output the number of bounding boxes for each class
    for class_id, count in class_counts.items():
        print(f"Class ID {class_id}: {count} bounding boxes")
def run():
    print("\n------ YOLO Dataset class counter ------\n")
    input_path = Path(input("Enter the path to the dataset folder or labels folder: ").strip())

    # Determine if the input path is the dataset folder or labels folder
    if input_path.is_dir():
        if (input_path / 'labels').is_dir():
            labels_dir = input_path / 'labels'
        elif (input_path.parts[-1] == 'labels') and input_path.is_dir():
            labels_dir = input_path
        else:
            print("Error: 'labels' folder not found in the provided path.")
            exit(1)
    else:
        print("Error: The provided path does not exist or is not a directory.")
        exit(1)

    # Count the number of bounding boxes for each class
    count_yolo_classes(labels_dir)

if __name__ == "__main__":
    
    run()