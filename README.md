# YOLO Dataset Tools

一系列工具，用於處理 YOLO 資料集，確保標籤文件和圖像文件的一致性，並進行必要的修改和檢查。

## 工具

### `yolo_all_datasets_checker.py`

檢查 YOLO 資料集的完整性。

- **功能**:
  - 確保圖像和標籤文件數量匹配
  - 檢查邊界框數量與 `data.yaml` 中的類別名稱對比
  - 確認 `data.yaml` 中類別名稱的存在

### `yolo_class_counter.py`

計算 YOLO 標籤文件中每個類別的邊界框數量。

- **功能**:
  - 顯示每個類別的邊界框數量

### `yolo_dataset_reducer.py`

移動或刪除 YOLO 資料集中的圖像和標籤文件。

- **功能**:
  - 移動或刪除圖像及標籤文件
  - 手動檢查模式

### `yolo_dataset_splitter.py`

將圖像和標籤文件移動到 `images` 和 `labels` 子資料夾中。

- **功能**:
  - 移動 `.jpg` 和 `.txt` 文件到目標子資料夾

### `yolo_dataset_status.py`

檢查 YOLO 資料集的狀態，包括圖像和標籤數量、類別 ID 和格式錯誤行。

- **功能**:
  - 計算圖像和標籤數量
  - 統計類別 ID 和標註框數量
  - 檢查並修正格式錯誤行

### `yolo_extract_background_data.py`

將沒有對應標籤或標籤為空的圖像移動到新資料夾，並創建空標籤文件。

- **功能**:
  - 移動無標籤或空標籤的圖像
  - 創建空標籤文件

### `yolo_file_checker.py`

檢查圖像和標籤文件的一致性，刪除不匹配的標籤文件，並提示用戶刪除沒有對應標籤的圖像。

- **功能**:
  - 確保圖像和標籤數量匹配
  - 處理不匹配的圖像和標籤文件

### `yolo_find_target_class_files.py`

查找僅包含指定目標類別的標籤文件。

- **功能**:
  - 列出僅包含目標類別的標籤文件

### `yolo_modify_labels.py`

根據映射修改標籤文件中的類別 ID。

- **功能**:
  - 替換標籤文件中的類別 ID

### `yolo_remove_class_labels.py`

從標籤文件中刪除指定類別編號的行。

- **功能**:
  - 移除包含指定類別 ID 的行
