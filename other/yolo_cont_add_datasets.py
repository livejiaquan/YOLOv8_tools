import os
import shutil

def get_next_index(folder):
    """获取文件夹中最大的文件编号"""
    files = [f for f in os.listdir(folder) if f.endswith('.txt')]
    if not files:
        return 0
    indices = [int(os.path.splitext(f)[0]) for f in files]
    return max(indices) + 1

def copy_yolo_data(source_path, target_path):
    source_images_folder = os.path.join(source_path, "images")
    source_labels_folder = os.path.join(source_path, "labels")
    target_images_folder = os.path.join(target_path, "images")
    target_labels_folder = os.path.join(target_path, "labels")
    
    # 创建目标文件夹
    os.makedirs(target_images_folder, exist_ok=True)
    os.makedirs(target_labels_folder, exist_ok=True)
    
    # 获取目标文件夹中下一个文件编号
    next_index = get_next_index(target_labels_folder)
    
    # 复制并重命名文件
    for label_file in os.listdir(source_labels_folder):
        base_name = f"{next_index:08}"
        
        source_label_path = os.path.join(source_labels_folder, label_file)
        target_label_path = os.path.join(target_labels_folder, f"{base_name}.txt")
        
        source_image_path = os.path.join(source_images_folder, label_file.replace('.txt', '.jpg'))
        target_image_path = os.path.join(target_images_folder, f"{base_name}.jpg")
        
        if os.path.exists(source_image_path):
            shutil.copy(source_image_path, target_image_path)
            shutil.copy(source_label_path, target_label_path)
            next_index += 1
        else:
            print(f"Warning: Image file {source_image_path} does not exist for label {source_label_path}. Skipping this pair.")

if __name__ == "__main__":
    # 來源資料夾路徑
    source_path = r"D:\YOLOv8_data\b_ppl_car_total"
    
    # 目標資料夾路徑
    target_path = r"D:\YOLOv8_data\0821_ppl_car"
    
    copy_yolo_data(source_path, target_path)
    
    print("Data copying and renaming completed.")
