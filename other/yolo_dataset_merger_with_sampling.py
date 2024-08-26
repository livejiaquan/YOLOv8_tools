import os
import shutil
import random

def merge_datasets(source_dirs, target_dir, sample_percentage=None):
    """
    Merge multiple datasets by copying image and label files from source directories 
    into the specified target directory. Each dataset is expected to have 'images' 
    and 'labels' subdirectories.

    Args:
    - source_dirs (list): List of paths to source dataset directories.
    - target_dir (str): Path to the target dataset directory where the merged data will be stored.
    - sample_percentage (float, optional): Percentage of data to sample from each source directory. 
                                             If None, all data will be used. Default is None.
    """
    # Create target directories for images and labels if they don't exist
    os.makedirs(os.path.join(target_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(target_dir, 'labels'), exist_ok=True)
    
    image_counter = 0
    source_data_count = {}

    # Iterate through source directories
    for source_dir in source_dirs:
        image_dir = os.path.join(source_dir, 'images')
        label_dir = os.path.join(source_dir, 'labels')

        # List all image files in the source directory
        image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
        
        # Calculate the number of images to sample based on the percentage
        if sample_percentage:
            num_images_to_sample = int(len(image_files) * sample_percentage / 100)
            sampled_images = random.sample(image_files, num_images_to_sample)
        else:
            sampled_images = image_files

        # Update source_data_count dictionary
        source_name = os.path.basename(source_dir)
        source_data_count[source_name] = len(sampled_images)

        # Iterate through sampled image files
        for image_file in sampled_images:
            label_file = image_file[:-4] + '.txt'
            
            # Check if corresponding label file exists
            if os.path.exists(os.path.join(label_dir, label_file)):
                image_counter += 1
                
                # Generate new file names for copied image and label files
                new_image_name = f'{image_counter:08}.jpg'
                new_label_name = f'{image_counter:08}.txt'
                
                # Define target paths for copied image and label files
                target_image_path = os.path.join(target_dir, 'images', new_image_name)
                target_label_path = os.path.join(target_dir, 'labels', new_label_name)
                
                # Copy image and label files to the target directory
                shutil.copy(os.path.join(image_dir, image_file), target_image_path)
                shutil.copy(os.path.join(label_dir, label_file), target_label_path)

    # Print sampled data count for each source directory
    print("Sampled data count for each source directory:")
    for source, count in source_data_count.items():
        print(f"{source}: {count} samples")

if __name__ == "__main__":
    # Define paths to source dataset directories and target dataset directory
    source_dirs = [
        r"C:\Users\limjiaquan\OneDrive - 台聚管理顧問股份有限公司\桌面\LIM JIA QUAN\0124\20240119_08_45",
        r"C:\Users\limjiaquan\OneDrive - 台聚管理顧問股份有限公司\桌面\LIM JIA QUAN\0221\2024_2_15_06_48"
        # MORE SOURCE...
    ]
    
    target_dir = r"C:\Users\limjiaquan\OneDrive - 台聚管理顧問股份有限公司\桌面\LIM JIA QUAN\0124\totalv5"

    # Define sample percentage (e.g., 1%)
    sample_percentage = 10  # Set to None if you want to use all data
    
    # Merge datasets
    merge_datasets(source_dirs, target_dir, sample_percentage)

