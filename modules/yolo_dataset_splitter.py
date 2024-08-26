import os
import shutil

def move_files(source_folder):
    # 定义目标文件夹路径
    target_images_path = os.path.join(source_folder, "images")
    target_labels_path = os.path.join(source_folder, "labels")

    # 检查目标文件夹是否已经存在
    if os.path.exists(target_images_path) and os.path.exists(target_labels_path):
        print(f"Images and labels folders already exist in {source_folder}. Exiting without further actions.")
        return False

    # 创建目标文件夹
    os.makedirs(target_images_path, exist_ok=True)
    os.makedirs(target_labels_path, exist_ok=True)

    # 遍历原始数据集文件夹中的所有文件
    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            # 如果是图片文件，则移动到目标图片文件夹中
            shutil.move(os.path.join(source_folder, file), os.path.join(target_images_path, file))
        elif file.endswith(".txt"):
            # 如果是标签文件，则移动到目标标签文件夹中
            shutil.move(os.path.join(source_folder, file), os.path.join(target_labels_path, file))

    print(f"Files from {source_folder} have been moved successfully!")
    return True
def run():
    print("\n------ YOLO Dataset Splitter ------\n")
    source_folder = input("Enter the path to the source dataset folder: ").strip()
    
    # 移动文件
    if move_files(source_folder):
        print("All files have been moved successfully!")

if __name__ == "__main__":
    
    run()