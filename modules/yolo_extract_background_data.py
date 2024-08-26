import os
import shutil

def organize_yolo_dataset(base_path):
    """
    Organize YOLO dataset by moving images without corresponding labels or with empty labels to a new folder
    and creating empty label files.

    Args:
    - base_path (str): Root folder path containing 'images' and 'labels' subfolders.
    """
    try:
        # Set paths for 'images' and 'labels' folders
        images_path = os.path.join(base_path, 'images')
        labels_path = os.path.join(base_path, 'labels')
        
        # Check if 'images' and 'labels' folders exist
        if not os.path.exists(images_path) or not os.path.exists(labels_path):
            print("Images or labels folder does not exist.")
            return

        # Get list of file names in 'images' and 'labels' folders
        images_files = [f for f in os.listdir(images_path) if f.endswith('.jpg')]
        labels_files = [f for f in os.listdir(labels_path) if f.endswith('.txt')]

        # Check if there are images without corresponding labels or with empty labels
        files_to_move = []
        for image_file in images_files:
            label_file = image_file.replace('.jpg', '.txt')
            src_image_path = os.path.join(images_path, image_file)
            src_label_path = os.path.join(labels_path, label_file)
            
            # Check if label file exists and if it's not empty
            if not os.path.exists(src_label_path) or os.path.getsize(src_label_path) == 0:
                files_to_move.append((src_image_path, image_file, label_file))

        # If there are no files to move, return without further action
        if not files_to_move:
            print("No background files need to be moved.")
            return

        # Create new folder prefixed with 'b_' using base folder name
        base_folder_name = os.path.basename(base_path)
        b_folder_name = f"b_{base_folder_name}"
        b_folder_path = os.path.join(base_path, b_folder_name)
        b_images_path = os.path.join(b_folder_path, 'images')
        b_labels_path = os.path.join(b_folder_path, 'labels')

        # Create 'b_', 'b_/images', and 'b_/labels' folders if they do not exist
        os.makedirs(b_folder_path, exist_ok=True)
        os.makedirs(b_images_path, exist_ok=True)
        os.makedirs(b_labels_path, exist_ok=True)

        # Move images without corresponding labels or with empty labels to 'b_/images' 
        # and create empty label files in 'b_/labels'
        for src_image_path, image_file, label_file in files_to_move:
            # Move image file to 'b_/images'
            dest_image_path = os.path.join(b_images_path, image_file)
            shutil.move(src_image_path, dest_image_path)
            
            # Create empty .txt file in 'b_/labels' with the same name as the moved image file
            dest_label_path = os.path.join(b_labels_path, label_file)
            with open(dest_label_path, 'w') as f:
                pass

        print("Extract background data successfully.")
    
    except Exception as e:
        print(f"An error occurred during execution: {e}")

def run():
    """
    Run function to execute the dataset organization process.
    """
    print("\n------ YOLO Dataset Background Extractor ------\n")
    base_path = input("Enter the path to the dataset root folder: ").strip()
    organize_yolo_dataset(base_path)

if __name__ == "__main__":
    
    run()
