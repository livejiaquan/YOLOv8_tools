import os
import json

def count_class_in_txt(file_path, class_ids):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    count = {class_id: 0 for class_id in class_ids}
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        if class_id in count:
            count[class_id] += 1
    return count

def count_class_in_json(json_data, image_id, class_ids):
    count = {class_id: 0 for class_id in class_ids}
    for item in json_data:
        if item['image_id'] == image_id and item['category_id'] in count:
            count[item['category_id']] += 1
    return count

def check_labels_and_predictions(labels_dir, json_file, class_ids):
    # Load JSON data
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    discrepancies = []

    # Check each txt file in labels directory
    for txt_file in os.listdir(labels_dir):
        if txt_file.endswith('.txt'):
            image_id = int(txt_file.split('.')[0])
            txt_file_path = os.path.join(labels_dir, txt_file)
            label_count = count_class_in_txt(txt_file_path, class_ids)
            prediction_count = count_class_in_json(json_data, image_id, class_ids)

            for class_id in class_ids:
                if label_count[class_id] != prediction_count[class_id]:
                    discrepancies.append((image_id, class_id, label_count[class_id], prediction_count[class_id]))

    # Print discrepancies
    if discrepancies:
        print("Discrepancies found:")
        for discrepancy in discrepancies:
            print(f"Image ID: {discrepancy[0]}, Class ID: {discrepancy[1]}, Label Count: {discrepancy[2]}, Prediction Count: {discrepancy[3]}")
    else:
        print("No discrepancies found.")

# Example usage:
labels_dir = r'D:\YOLOv8_data\0802_ppl_car_split\labels\val'
json_file = r'D:\YOLOv8_data\predictions.json'
class_ids = [1]  # Specify the class IDs you want to check

check_labels_and_predictions(labels_dir, json_file, class_ids)
