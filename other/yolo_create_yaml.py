import os

def generate_data_yaml(source_path, classes):
    # 設定檔案路徑
    yaml_path = os.path.join(source_path, "data.yaml")
    
    # 寫入data.yaml檔案
    with open(yaml_path, 'w') as f:
        f.write("comments: made by XX\n")
        f.write(f"nc: {len(classes)}\n")
        f.write("names:\n")
        for idx, cls in enumerate(classes):
            f.write(f"  {idx}: {cls}\n")

def generate_data_yaml_in_subfolders(root_path, classes):
    # 遍歷root_path下的所有子資料夾
    for root, dirs, _ in os.walk(root_path):
        # 檢查是否包含images和labels資料夾
        if 'images' in dirs and 'labels' in dirs:
            generate_data_yaml(root, classes)
            print(f"data.yaml has been generated at {root}")

if __name__ == "__main__":
    # 資料集路徑
    root_path = r"D:\YOLOv8_data\JQ_RTSP_v2\cam19_20240729_1009"
    
    # 設定資料集類別
    classes = [
        "person",
        "truck"
    ]
    
    generate_data_yaml_in_subfolders(root_path, classes)
