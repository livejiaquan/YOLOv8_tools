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

### `generate_bat.py`

自動生成批處理文件，用於在特定的 Conda 環境中執行 Python 腳本並處理 RTSP 視頻流。

- **功能**:
  - 讀取 `config.yaml` 配置 Conda 環境和 Python 腳本路徑
  - 生成批處理文件並配置 RTSP URL

### `pngtojpg.py`

將指定文件夾中的 PNG 圖像轉換為 JPG 格式。

- **功能**:
  - 遍歷文件夾中的 PNG 圖像
  - 轉換為 JPG 格式並可選擇刪除原 PNG 文件

### `yolo_cont_add_datasets.py`

將 YOLO 數據集中的圖像和標籤文件從源文件夾複製到目標文件夾，並按編號格式重命名。

- **功能**:
  - 創建目標文件夾中的 `images` 和 `labels` 子文件夾
  - 複製並重命名圖像和標籤文件

### `yolo_create_yaml.py`

自動生成 YOLO 數據集所需的 `data.yaml` 文件。

- **功能**:
  - 生成 `data.yaml` 文件，包括數據集的類別數量和名稱
  - 遞歸遍歷子文件夾生成配置文件

### `yolo_dataset_merger_with_sampling.py`

合併多個 YOLO 數據集，並可選擇性地對每個源數據進行隨機採樣。

- **功能**:
  - 合併來源目錄中的圖像和標籤文件
  - 支持隨機採樣功能，重命名文件以確保唯一性

### `yolo_extra_new.py`

從多個子文件夾中提取和重命名 YOLO 數據集的圖像和標籤文件，並進行類別映射。

- **功能**:
  - 提取和重命名圖像和標籤文件
  - 根據 `data.yaml` 進行類別 ID 轉換
  - 生成新的 `data.yaml` 文件

### `yolo_merge_datasets.py`

將多個資料集的圖像和標籤文件合併到一個目標資料夾中。

- **功能**:
  - 創建目標資料夾中的 `images` 和 `labels` 子目錄
  - 複製和重命名來源資料夾中的文件

### `yolo_merge_labels.py`

合併新標籤資料夾中的標籤檔案到原始標籤資料夾中。

- **功能**:
  - 將新標籤附加到現有標籤檔案中
  - 確保每行以換行符結束

### `yolo_split_train_val.py`

按比例將圖像和標籤文件劃分為訓練集、驗證集和測試集。

- **功能**:
  - 移動或複製文件到指定的輸出目錄
  - 生成 `train.txt`、`val.txt` 和 `test.txt` 文件包含文件路徑


### `main.py`

動態加載並執行模組中的功能。

- **功能**:
  - 列出 `modules` 目錄下的所有模組（排除 `__init__.py` 文件）
  - 根據用戶選擇執行模組中的 `run` 函數
  - 支持通過輸入 `'q'` 退出程序
