import pandas as pd
import os
import yaml

def update_comments_from_csv():
    source_path = r"C:\Users\limjiaquan\YOLOv8_data\test_ppe"  # 資料集路徑
    csv_path = r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\20240527_1316_YOLO_dataset_check.csv"  # CSV文件路徑
    
    # 讀取CSV文件
    df = pd.read_csv(csv_path)
    df['Comments'] = df['Comments'].fillna('')  # 將NaN值轉換為空字符串
    
    for _, row in df.iterrows():
        folder_path = os.path.join(source_path, row['Folder'])
        data_yaml_path = os.path.join(folder_path, 'data.yaml')
        
        # 檢查資料集是否存在
        if not os.path.exists(folder_path) or not os.path.exists(data_yaml_path):
            print(f"Error: Data set not found for folder '{row['Folder']}'")
            continue
        
        # 讀取現有的data.yaml內容
        with open(data_yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        
        # 更新或新增comments
        data['comments'] = row['Comments'].strip()
        
        # 寫回data.yaml文件
        with open(data_yaml_path, 'w') as f:
            yaml.safe_dump(data, f, default_flow_style=False)

if __name__ == "__main__":
    update_comments_from_csv()
