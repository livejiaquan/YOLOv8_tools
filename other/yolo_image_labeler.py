import os
import cv2
import yaml
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

# 加載類別名稱
def load_classes(data_file):
    with open(data_file, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data['names']

# 繪製圖像上的邊界框
def draw_boxes(image, labels, class_names):
    num_classes = len(class_names)
    
    # 固定的顔色列表
    colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128)]
    
    for label in labels:
        class_id, x_center, y_center, width, height = label
        class_name = class_names[int(class_id)]
        
        x1 = int((x_center - width / 2) * image.shape[1])
        y1 = int((y_center - height / 2) * image.shape[0])
        x2 = int((x_center + width / 2) * image.shape[1])
        y2 = int((y_center + height / 2) * image.shape[0])
        
        color = colors[int(class_id) % len(colors)]
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        
        label_text = f"{int(class_id)}: {class_name}"
        cv2.putText(image, label_text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # 在圖像的右上角顯示類別名稱
    class_names_str = ', '.join([f"{key}: {value}" for key, value in class_names.items()])
    cv2.putText(image, class_names_str, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

# 更新標籤
def update_label(label_path, labels):
    with open(label_path, 'w') as file:
        for label in labels:
            file.write(' '.join(map(str, label)) + '\n')

# 鼠標點擊事件處理
def handle_mouse_event(event, x, y, flags, param):
    global labels, label_path, class_names, image, image_path, window_name
    
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        # Find the label to change based on the mouse click
        for i, label in enumerate(labels):
            class_id, x_center, y_center, width, height = label
            x1 = int((x_center - width / 2) * image.shape[1])
            y1 = int((y_center - height / 2) * image.shape[0])
            x2 = int((x_center + width / 2) * image.shape[1])
            y2 = int((y_center + height / 2) * image.shape[0])
            
            if x1 <= x <= x2 and y1 <= y <= y2:
                if event == cv2.EVENT_LBUTTONDOWN:
                    new_class_id = (class_id + 1) % len(class_names)
                else: # event == cv2.EVENT_RBUTTONDOWN
                    new_class_id = (class_id - 1) % len(class_names)
                
                labels[i][0] = new_class_id
                update_label(label_path, labels)
                
                # Reload image and labels
                image = cv2.imread(image_path)
                if image is None:
                    messagebox.showerror("Error", f"Error loading image: {image_path}")
                    return
                
                draw_boxes(image, labels, class_names)
                cv2.imshow(window_name, image)
                break

# 處理選擇的資料夾
def process_folder(source):
    global labels, label_path, class_names, image, image_path, window_name
    
    image_folder = os.path.join(source, 'images')
    label_folder = os.path.join(source, 'labels')
    data_file = os.path.join(source, 'data.yaml')
    
    # 檢查是否存在必要的資料夾和文件
    if not (os.path.exists(image_folder) and os.path.exists(label_folder) and os.path.exists(data_file)):
        messagebox.showerror("Error", "Selected folder must contain 'images', 'labels', and 'data.yaml' files.")
        return
    
    class_names = load_classes(data_file)
    
    image_files = [filename for filename in os.listdir(image_folder) if filename.endswith('.jpg') or filename.endswith('.png')]
    total_images = len(image_files)
    current_index = 0
    
    window_name = 'Image'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setMouseCallback(window_name, handle_mouse_event)
    
    while True:
        filename = image_files[current_index]
        image_path = os.path.join(image_folder, filename)
        label_path = os.path.join(label_folder, filename.replace('.jpg', '.txt').replace('.png', '.txt'))
        
        if os.path.exists(label_path):
            with open(label_path, 'r') as file:
                lines = file.readlines()
                labels = [list(map(float, line.strip().split())) for line in lines]
            
            image = cv2.imread(image_path)
            if image is None:
                messagebox.showerror("Error", f"Error loading image: {image_path}")
                continue
            
            draw_boxes(image, labels, class_names)
            
            cv2.setWindowTitle(window_name, f'Image ({current_index + 1}/{total_images})')
            cv2.imshow(window_name, image)
            
            key = cv2.waitKey(0)
            
            if key == 27:
                break
            elif key == ord('d'):
                current_index = (current_index + 1) % total_images
            elif key == ord('a'):
                current_index = (current_index - 1) % total_images
            elif key == ord('e'):
                current_index = (current_index + 20) % total_images
            elif key == ord('q'):
                current_index = (current_index - 20) % total_images

    cv2.destroyAllWindows()

# 選擇資料夾
def select_folder():
    source = filedialog.askdirectory()
    if source:
        process_folder(source)
# 創建窗口和按鈕
root = tk.Tk()
root.title("Image Labeler")
root.geometry("500x400")

label = ttk.Label(root, text=   "Please select a directory with the following structure:\n\n"
                                "- datasets\n"
                                "  - images\n"
                                "  - labels\n"
                                "  - data.yaml\n\n"
                                "Usage Instructions:\n\n"
                                "- 'd'                  : Next image.\n"
                                "- 'a'                  : Previous image.\n"
                                "- 'e'                  : Jump forward 20 images.\n"
                                "- 'q'                  : Jump back 20 images.\n"
                                "- Left-click      : change to next class.\n"
                                "- Right-click   : change to previous class.\n"
                                "- 'ESC'             : Exit program."
                                )
label.pack(pady=20)

select_button = ttk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

root.mainloop()
