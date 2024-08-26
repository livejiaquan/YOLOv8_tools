import os

def merge_labels(labels_path, new_labels_path):
    # 確保labels和labels_new資料夾都存在
    if not os.path.exists(labels_path) or not os.path.exists(new_labels_path):
        print("Error: labels or labels_new folder does not exist.")
        return
    
    # 遍歷labels_new資料夾中的每個標籤檔案
    for filename in os.listdir(new_labels_path):
        if filename.endswith('.txt'):
            new_filepath = os.path.join(new_labels_path, filename)
            final_filepath = os.path.join(labels_path, filename)
            
            # 讀取新的標籤檔案內容
            with open(new_filepath, 'r') as f:
                new_lines = f.readlines()
            
            # 確保每行都有換行符
            new_lines = [line.rstrip('\n') + '\n' for line in new_lines]
            
            # 檢查final_labels_path文件是否有内容
            if os.path.exists(final_filepath):
                with open(final_filepath, 'r') as f:
                    existing_content = f.read()
                
                # 如果文件内容不是空的，并且最后一个字符不是换行符，则添加一个换行符
                if existing_content and not existing_content.endswith('\n'):
                    with open(final_filepath, 'a') as f:
                        f.write('\n')
            
            # 寫入新的標籤到final_labels_path檔案
            with open(final_filepath, 'a') as f:
                for line in new_lines:
                    f.write(line)
                    # 調試信息，檢查每次寫入的行
                    print(f"Writing line to {final_filepath}: {line.strip()}")

if __name__ == "__main__":
    # 定義labels和labels_new資料夾的路徑
    labels_path = r"C:\Users\limjiaquan\Downloads\labels\labels"          # 原始標籤檔案資料夾
    new_labels_path = r"C:\Users\limjiaquan\Downloads\person\labels"  # 新增的標籤檔案資料夾
    
    # 合併新的標籤檔案
    merge_labels(labels_path, new_labels_path)
    print("Merging labels completed.")
