import os
import shutil
import random
import tkinter as tk
from tkinter import filedialog, messagebox

def merge_datasets(source_dirs, target_dir, sample_percentage=None):
    os.makedirs(os.path.join(target_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(target_dir, 'labels'), exist_ok=True)
    
    image_counter = 0
    source_counts = {}

    for source_dir in source_dirs:
        image_dir = os.path.join(source_dir, 'images')
        label_dir = os.path.join(source_dir, 'labels')

        image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
        
        if sample_percentage:
            num_images_to_sample = int(len(image_files) * sample_percentage / 100)
            sampled_images = random.sample(image_files, num_images_to_sample)
        else:
            sampled_images = image_files

        source_name = os.path.basename(source_dir)
        source_counts[source_name] = len(sampled_images)
        
        for image_file in sampled_images:
            label_file = image_file[:-4] + '.txt'
            
            if os.path.exists(os.path.join(label_dir, label_file)):
                image_counter += 1
                
                new_image_name = f'{image_counter:08}.jpg'
                new_label_name = f'{image_counter:08}.txt'
                
                target_image_path = os.path.join(target_dir, 'images', new_image_name)
                target_label_path = os.path.join(target_dir, 'labels', new_label_name)
                
                shutil.copy(os.path.join(image_dir, image_file), target_image_path)
                shutil.copy(os.path.join(label_dir, label_file), target_label_path)

    return source_counts

def count_classes(labels_dir):
    class_counts = {}
    
    for label_file in os.listdir(labels_dir):
        with open(os.path.join(labels_dir, label_file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                class_id = line.split()[0]
                if class_id not in class_counts:
                    class_counts[class_id] = 0
                class_counts[class_id] += 1
    
    return class_counts

def add_source_dir():
    directory = filedialog.askdirectory(title="Select source directory")
    if directory:
        source_listbox.insert(tk.END, directory)

def remove_source_dir():
    selected_index = source_listbox.curselection()
    if selected_index:
        source_listbox.delete(selected_index)

def browse_target_dir():
    directory = filedialog.askdirectory(title="Select target directory", mustexist=True)
    if directory:
        target_var.set(directory)

def start_merge():
    source_dirs = source_listbox.get(0, tk.END)
    target_dir = target_var.get()
    sample_percentage = float(sample_var.get()) if sample_var.get() else None
    
    source_counts = merge_datasets(source_dirs, target_dir, sample_percentage)
    
    class_counts = count_classes(os.path.join(target_dir, 'labels'))
    
    result = "Data count for each source directory:\n"
    for source, count in source_counts.items():
        result += f"{source} : {count} \n"
    
    result += "\nClasses counts:\n"
    for class_id, count in class_counts.items():
        result += f"classes {class_id}: {count} samples\n"
    
    result_label.config(text=result)

root = tk.Tk()
root.title("Dataset Merger")

source_var = tk.StringVar()
target_var = tk.StringVar()
sample_var = tk.StringVar()

source_label = tk.Label(root, text="Source Directories:")
source_label.pack()

source_listbox = tk.Listbox(root, width=60, selectmode=tk.SINGLE)
source_listbox.pack()

add_button = tk.Button(root, text="Add", command=add_source_dir)
add_button.pack()

remove_button = tk.Button(root, text="Remove", command=remove_source_dir)
remove_button.pack()

target_label = tk.Label(root, text="Target Directory:")
target_label.pack()

target_entry = tk.Entry(root, textvariable=target_var, width=60)
target_entry.pack()

browse_target_button = tk.Button(root, text="Browse", command=browse_target_dir)
browse_target_button.pack()

sample_label = tk.Label(root, text="Sample Percentage (0-100%):")
sample_label.pack()

sample_entry = tk.Entry(root, textvariable=sample_var, width=10)
sample_entry.pack()

start_button = tk.Button(root, text="Start Merge", command=start_merge)
start_button.pack()

result_label = tk.Label(root, text="", wraplength=400, justify=tk.LEFT)
result_label.pack()

root.mainloop()
