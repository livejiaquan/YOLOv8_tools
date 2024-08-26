import os
import shutil
import yaml

def extract_and_rename(source_folders, class_mapping, output_path):
    output_images_folder = os.path.join(output_path, "images")
    output_labels_folder = os.path.join(output_path, "labels")
    os.makedirs(output_images_folder, exist_ok=True)
    os.makedirs(output_labels_folder, exist_ok=True)
    
    counter = 0
    all_classes = set()
    sorted_classes = sorted(class_mapping.keys(), key=lambda x: class_mapping[x])
    
    for source_folder in source_folders:
        labels_folder = os.path.join(source_folder, "labels")
        images_folder = os.path.join(source_folder, "images")
        
        # Load class names from data.yaml
        with open(os.path.join(source_folder, "data.yaml"), 'r') as f:
            data = yaml.safe_load(f)
            class_names = data['names']
        
        for label_file in os.listdir(labels_folder):
            with open(os.path.join(labels_folder, label_file), 'r') as f:
                lines = f.readlines()
            
            new_lines = []
            for line in lines:
                try:
                    class_id_file = int(float(line.split()[0]))
                    class_name_file = class_names[class_id_file]
                    
                    if class_name_file in class_mapping:
                        # Update class id based on class name
                        new_class_id = class_mapping[class_name_file]
                        line = f"{new_class_id} {' '.join(line.split()[1:])}"
                        new_lines.append(line)
                        all_classes.add(class_name_file)
                except ValueError:
                    pass
            
            if new_lines:
                # Write new label file
                with open(os.path.join(output_labels_folder, f"{counter:08}.txt"), 'w') as f:
                    f.write("\n".join(new_lines))
                
                # Copy corresponding image file
                image_file = label_file.replace('.txt', '.jpg')  # Assuming jpg images
                shutil.copy(os.path.join(images_folder, image_file), os.path.join(output_images_folder, f"{counter:08}.jpg"))
                
                counter += 1

    # Write new data.yaml
    with open(os.path.join(output_path, "data.yaml"), 'w') as f:
        f.write("nc: {}\n".format(len(all_classes)))
        f.write("names:\n")
        for idx, class_name in enumerate(sorted_classes):
            f.write(f"  {idx}: {class_name}\n")
                
if __name__ == "__main__":
    # 資料夾路徑
    source_folders = [
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240223_1008",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240227_0932",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240417_0953",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240423_0138",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240417_1605",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240422_1048",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240408_0843",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240423_0842",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240422_0238",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240426_0426",
        r"C:\Users\limjiaquan\桌面\0513\person",
        r"C:\Users\limjiaquan\桌面\0513\cam16_20240422_predict5",
        r"C:\Users\limjiaquan\桌面\0513\cam17_20240507_1008",
        r"C:\Users\limjiaquan\桌面\0513\camXX_20231026_0006",
        r"C:\Users\limjiaquan\桌面\0513\camXX_20231026_0012",
        r"C:\Users\limjiaquan\桌面\0513\camXX_20231026_0011",
        r"C:\Users\limjiaquan\桌面\0513\cam82_20240507_1014",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240507_1010",
        r"C:\Users\limjiaquan\桌面\0513\cam19_20240507",
        r"C:\Users\limjiaquan\桌面\0513\cam16_20240430_1031",
        r"C:\Users\limjiaquan\桌面\0513\cam17_20240429_1004",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240415_0904",
        r"C:\Users\limjiaquan\桌面\0513\cam81_20240416_0352",
        r"C:\Users\limjiaquan\桌面\0513\cmm81_20240429_1009",
        r"C:\Users\limjiaquan\桌面\0513\cam16_20240419_0245"

        
        
    ]
    
    # 要提取的類別名稱和新的類別ID的mapping
    class_mapping = {
        'person': 0,
        'pack': 1

    }
    
    # 輸出路徑
    output_path = r"C:\Users\limjiaquan\桌面\pack_v8"
    
    extract_and_rename(source_folders, class_mapping, output_path)
    
    print("Extraction and renaming completed.")

