import os
import shutil

def merge_datasets(source_dirs, target_dir):
    """
    Merge multiple datasets by copying image and label files from source directories 
    into the specified target directory. Each dataset is expected to have 'images' 
    and 'labels' subdirectories.

    Args:
    - source_dirs (list): List of paths to source dataset directories.
    - target_dir (str): Path to the target dataset directory where the merged data will be stored.
    """
    # Create target directories for images and labels if they don't exist
    os.makedirs(os.path.join(target_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(target_dir, 'labels'), exist_ok=True)
    image_counter = 0
    
    # Iterate through source directories
    for source_dir in source_dirs:
        image_dir = os.path.join(source_dir, 'images')
        label_dir = os.path.join(source_dir, 'labels')
        
        # Iterate through label files in each source directory
        for label_file in os.listdir(label_dir):
            if label_file.endswith('.txt'):
                # Get corresponding image file path
                image_file = os.path.join(image_dir, label_file[:-4] + '.jpg')
                if os.path.exists(image_file):
                    image_counter += 1
                    # Generate new file names for copied image and label files
                    new_image_name = f'{image_counter:08}.jpg'
                    new_label_name = f'{image_counter:08}.txt'
                    
                    # Define target paths for copied image and label files
                    target_image_path = os.path.join(target_dir, 'images', new_image_name)
                    target_label_path = os.path.join(target_dir, 'labels', new_label_name)
                    
                    # Copy image and label files to the target directory
                    shutil.copy(image_file, target_image_path)
                    shutil.copy(os.path.join(label_dir, label_file), target_label_path)

if __name__ == "__main__":
    # Define paths to source dataset directories and target dataset directory
    source_dirs = [
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam16_20240419_0245",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam16_20240422_predict5",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam16_20240430_1031",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam17_20240429_1004",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam17_20240507_1008",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam19_20240507",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240223_1008",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240227_0932",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240408_0843",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240415_0904",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240416_0352",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240417_0953",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240417_1605",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240422_0238",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240422_1048",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240423_0138",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240423_0842",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240426_0426",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240507_1010",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam81_20240517_0908",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam82_20240507_1014",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\camXX_20231026_0006",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\camXX_20231026_0011",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\camXX_20231026_0012",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cmm81_20240429_1009",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cmm81_20240517_1002",
        r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\person"
        
        # Add more source dataset paths as needed
    ]
    target_dir = "/Users/limjiaquan/YOLOv8_data/ppe_v2"

    # Merge datasets
    merge_datasets(source_dirs, target_dir)
