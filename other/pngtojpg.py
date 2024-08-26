from PIL import Image
import os

# 指定要转换的文件夹路径
folder_path = '/Users/limjiaquan/YOLOv8_data/cus_data/01_Project/07_0411hao/images'

# 循环遍历文件夹中的每个文件
for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        # 构建图像文件的完整路径
        image_path = os.path.join(folder_path, filename)
        
        # 打开 PNG 图像文件
        png_image = Image.open(image_path)
        
        # 生成新的文件名，将 .png 后缀替换为 .jpg
        new_filename = os.path.splitext(filename)[0] + '.jpg'
        
        # 构建新的图像文件完整路径
        new_image_path = os.path.join(folder_path, new_filename)
        
        # 将 PNG 图像保存为 JPG 格式
        png_image.convert('RGB').save(new_image_path, 'JPEG')
        
        # 关闭图像文件
        png_image.close()
        
        # 删除原始的 PNG 文件（可选）
        # os.remove(image_path)

print("Conversion completed.")
