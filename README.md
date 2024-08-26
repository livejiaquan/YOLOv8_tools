# YOLO Dataset Tools

A collection of tools for processing YOLO datasets, ensuring consistency between label files and images, and performing necessary modifications and checks.

## How to Use

To view the documentation in Traditional Chinese, [繁體中文](./README.zh_TW.md).

## Tools

### `main.py`

Dynamically loads and executes functions from modules.

- **Functionality**:
  - Lists all modules in the `modules` directory (excluding `__init__.py` files)
  - Executes the `run` function in the selected module based on user input
  - Allows exiting the program by entering `'q'`

### `yolo_all_datasets_checker.py`

Checks the integrity of YOLO datasets.

- **Functionality**:
  - Ensures image and label file counts match
  - Compares bounding box counts with category names in `data.yaml`
  - Verifies the existence of category names in `data.yaml`

### `yolo_class_counter.py`

Counts the number of bounding boxes for each class in YOLO label files.

- **Functionality**:
  - Displays the number of bounding boxes for each class

### `yolo_dataset_reducer.py`

Moves or deletes images and label files in YOLO datasets.

- **Functionality**:
  - Moves or deletes images and label files
  - Includes manual inspection mode

### `yolo_dataset_splitter.py`

Moves image and label files into `images` and `labels` subfolders.

- **Functionality**:
  - Moves `.jpg` and `.txt` files to the target subfolders

### `yolo_dataset_status.py`

Checks the status of YOLO datasets, including image and label counts, class IDs, and format errors.

- **Functionality**:
  - Calculates image and label counts
  - Statistics on class IDs and annotation box counts
  - Checks and corrects format errors

### `yolo_extract_background_data.py`

Moves images without corresponding labels or with empty labels to a new folder and creates empty label files.

- **Functionality**:
  - Moves unlabeled or empty-labeled images
  - Creates empty label files

### `yolo_file_checker.py`

Checks the consistency of image and label files, deletes unmatched label files, and prompts the user to delete images without corresponding labels.

- **Functionality**:
  - Ensures image and label counts match
  - Handles unmatched image and label files

### `yolo_find_target_class_files.py`

Finds label files that contain only specified target classes.

- **Functionality**:
  - Lists label files containing only target classes

### `yolo_modify_labels.py`

Modifies class IDs in label files according to a mapping.

- **Functionality**:
  - Replaces class IDs in label files

### `yolo_remove_class_labels.py`

Removes lines with specified class IDs from label files.

- **Functionality**:
  - Removes lines containing specified class IDs

### `generate_bat.py`

Automatically generates a batch file to execute a Python script in a specific Conda environment and process RTSP video streams.

- **Functionality**:
  - Reads `config.yaml` for Conda environment and Python script paths
  - Generates a batch file with RTSP URL configuration

### `pngtojpg.py`

Converts PNG images in a specified folder to JPG format.

- **Functionality**:
  - Traverses PNG images in a folder
  - Converts to JPG format and optionally deletes original PNG files

### `yolo_cont_add_datasets.py`

Copies and renames image and label files from source to target folders in YOLO datasets.

- **Functionality**:
  - Creates `images` and `labels` subfolders in the target folder
  - Copies and renames image and label files

### `yolo_create_yaml.py`

Automatically generates the `data.yaml` file required for YOLO datasets.

- **Functionality**:
  - Creates `data.yaml` file including dataset class counts and names
  - Recursively traverses subfolders to generate configuration files

### `yolo_dataset_merger_with_sampling.py`

Merges multiple YOLO datasets and optionally performs random sampling on source datasets.

- **Functionality**:
  - Merges image and label files from source directories
  - Supports random sampling with file renaming to ensure uniqueness

### `yolo_extra_new.py`

Extracts and renames YOLO dataset images and label files from multiple subfolders and performs class ID mapping.

- **Functionality**:
  - Extracts and renames image and label files
  - Converts class IDs according to `data.yaml`
  - Generates a new `data.yaml` file

### `yolo_merge_datasets.py`

Merges image and label files from multiple datasets into a single target folder.

- **Functionality**:
  - Creates `images` and `labels` subfolders in the target folder
  - Copies and renames files from source folders

### `yolo_merge_labels.py`

Merges label files from a new labels folder into an existing labels folder.

- **Functionality**:
  - Appends new labels to existing label files
  - Ensures each line ends with a newline character

### `yolo_split_train_val.py`

Splits image and label files into training, validation, and test sets by ratio.

- **Functionality**:
  - Moves or copies files to specified output directories
  - Generates `train.txt`, `val.txt`, and `test.txt` files with file paths
