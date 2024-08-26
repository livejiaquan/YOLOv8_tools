import os
import cv2
import tkinter as tk
from tkinter import filedialog

def process_images_labels():

    
    images_dir = images_dir_entry.get()
    labels_dir = labels_dir_entry.get()

    image_files = os.listdir(images_dir)
    total_images = len(image_files)
    current_index = 0

    current_index_label.config(text=f"Current Index: {current_index+1}/{total_images}")
    window.update()  # 更新窗口显示

    for image_file in image_files:
        if image_file.startswith('.'):
            continue

        image_path = os.path.join(images_dir, image_file)
        label_file = os.path.splitext(image_file)[0] + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        image = cv2.imread(image_path)

        with open(label_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                label_info = line.strip().split()
                class_id = int(label_info[0])
                x, y, w, h = map(float, label_info[1:5])

                start_x = int((x - w/2) * image.shape[1])
                start_y = int((y - h/2) * image.shape[0])
                end_x = int((x + w/2) * image.shape[1])
                end_y = int((y + h/2) * image.shape[0])
                cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

        cv2.imshow("Label Check", image)
        cv2.waitKey(0)

        current_index += 1
        current_index_label.config(text=f"Current Index: {current_index}/{total_images}")
        window.update()  # 更新窗口显示

    cv2.destroyAllWindows()


def browse_images_dir():
    images_dir = filedialog.askdirectory()
    images_dir_entry.delete(0, tk.END)
    images_dir_entry.insert(tk.END, images_dir)

def browse_labels_dir():
    labels_dir = filedialog.askdirectory()
    labels_dir_entry.delete(0, tk.END)
    labels_dir_entry.insert(tk.END, labels_dir)

window = tk.Tk()
window.title("Label Check")
window.geometry("500x250")

images_dir_label = tk.Label(window, text="Images Directory:")
images_dir_label.pack()
images_dir_entry = tk.Entry(window, width=50)
images_dir_entry.pack()
images_dir_button = tk.Button(window, text="Browse", command=browse_images_dir)
images_dir_button.pack()

labels_dir_label = tk.Label(window, text="Labels Directory:")
labels_dir_label.pack()
labels_dir_entry = tk.Entry(window, width=50)
labels_dir_entry.pack()
labels_dir_button = tk.Button(window, text="Browse", command=browse_labels_dir)
labels_dir_button.pack()

process_button = tk.Button(window, text="Process", command=process_images_labels)
process_button.pack()

current_index_label = tk.Label(window, text="Current Index: 0/0")
current_index_label.pack()

window.mainloop()
