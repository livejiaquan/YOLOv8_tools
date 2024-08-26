import os
import shutil

def move_files(source_folder, delete_count, manual_check=True):
    """
    Move or delete image and corresponding label files from the source folder.

    Args:
    - source_folder (str): The path to the source folder containing image and label files.
    - delete_count (int): Number of files to delete or move at a time.
    - manual_check (bool): If True, files are moved to a temporary folder for manual check before deletion. If False, files are deleted directly.
    """
    images_folder = os.path.join(source_folder, 'images')
    labels_folder = os.path.join(source_folder, 'labels')

    if not os.path.exists(images_folder) or not os.path.exists(labels_folder):
        print(f"Images or labels folder does not exist in the dataset path: {source_folder}.")
        return

    if manual_check:
        # Create a directory named 'temp_deleted_files' in the source folder
        temp_deleted_folder = os.path.join(source_folder, 'temp_deleted_files')
        if not os.path.exists(temp_deleted_folder):
            os.makedirs(temp_deleted_folder)
        temp_deleted_images = os.path.join(temp_deleted_folder, 'images')
        temp_deleted_labels = os.path.join(temp_deleted_folder, 'labels')
        os.makedirs(temp_deleted_images, exist_ok=True)
        os.makedirs(temp_deleted_labels, exist_ok=True)
    else:
        temp_deleted_images = None
        temp_deleted_labels = None

    # Get all .jpg files in the images folder
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]

    # Perform delete or move operations
    total_deleted = 0
    for i in range(0, len(image_files), delete_count + 1):
        for j in range(i, min(i + delete_count, len(image_files))):
            image_file = image_files[j]
            label_file = image_file.replace('.jpg', '.txt')
            image_path = os.path.join(images_folder, image_file)
            label_path = os.path.join(labels_folder, label_file)

            if manual_check:
                # Move files to the temporary folder
                shutil.move(image_path, temp_deleted_images)
                if os.path.exists(label_path):
                    shutil.move(label_path, temp_deleted_labels)
            else:
                # Delete files directly
                os.remove(image_path)
                if os.path.exists(label_path):
                    os.remove(label_path)
            total_deleted += 1

    if manual_check:
        print(f"{total_deleted} images and their labels have been moved to {temp_deleted_folder} for manual check before deletion.")
    else:
        print(f"{total_deleted} images and their labels have been deleted directly.")
def run():
    print("\n------ YOLO Dataset Reducer ------\n")
    print("This script moves or deletes image files and their corresponding label files from the source folder based on the specified delete count.")
    print("If manual check is enabled, the files will be moved to a temporary folder for manual review before deletion.")
    print("Otherwise, the files will be deleted directly.\n")

    # Get user inputs for source folder path, delete count, and manual check preference
    source_folder = input("Enter the path to the source folder containing image and label files: ").strip()
    try:
        delete_count = int(input("Enter the number of files to delete or move at a time: ").strip())
        manual_check = input("Do you want to enable manual check before deletion? (y/n): ").strip().lower() == 'y'
    except ValueError:
        print("Invalid input for delete count. Please enter a valid integer.")
        exit(1)

    # Move or delete files based on user inputs
    move_files(source_folder, delete_count, manual_check)
if __name__ == "__main__":
    run()
    
