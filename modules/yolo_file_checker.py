import os

def check_files(source_folder):
    """
    Check and synchronize image and label files in YOLO dataset folders.
    Remove mismatched label files and prompt user for mismatched images.

    Args:
    - source_folder (str): Root folder path containing 'images' and 'labels' subfolders.
    """
    images_folder = os.path.join(source_folder, 'images')
    labels_folder = os.path.join(source_folder, 'labels')
    
    # Get list of files in 'images' and 'labels' folders
    images_files = set(os.listdir(images_folder))
    labels_files = set(os.listdir(labels_folder))
    
    # Check for images without corresponding labels
    mismatched_images = [img for img in images_files if img.replace('.jpg', '.txt') not in labels_files]
    
    # If there are mismatched images, prompt for deletion
    if mismatched_images:
        print("\nImages without corresponding labels:")
        print(f"Number of mismatched images: {len(mismatched_images)}")
        decision = input("Do you want to delete all mismatched images? (y/n): ")
        if decision.lower() == 'y':
            for img in mismatched_images:
                img_path = os.path.join(images_folder, img)
                os.remove(img_path)
                print(f"Deleted mismatched image file: {img}")
            print("All mismatched images deleted.")
        else:
            print("No files deleted.")
    
    # Check for mismatched label files and delete them directly
    for label_file in list(labels_files):
        image_name = label_file.replace('.txt', '.jpg')
        if image_name not in images_files:
            os.remove(os.path.join(labels_folder, label_file))
            print(f"Deleted mismatched label file: {label_file}")
            labels_files.remove(label_file)
    
    # Check if number of images matches number of labels
    if len(images_files) != len(labels_files):
        print(f"\nMismatched file count - images: {len(images_files)}, labels: {len(labels_files)}")
    else:
        print(f"\nAll files are matched - images and labels count: {len(images_files)}")

def run():
    """
    Run function to execute the file checking process for YOLO dataset.
    """
    print("\n------ YOLO File Checker ------\n")
    source_folder = input("Enter the path to the dataset root folder: ").strip()
    check_files(source_folder)

if __name__ == "__main__":
    
    run()
