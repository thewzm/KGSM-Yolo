from PIL import Image
import os

# 输入和输出文件夹路径
input_folder = "input_images"
output_folder = "output_images"

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图像文件
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # 打开原始图像
        input_path = os.path.join(input_folder, filename)
        input_image = Image.open(input_path)

        # 计算缩放后的尺寸，保持宽高比
        width, height = input_image.size
        new_size = (640, int(640 * (height / width)))

        # 缩放图像
        resized_image = input_image.resize(new_size, Image.ANTIALIAS)

        # 创建一个新的白色背景图像
        output_image = Image.new("RGB", (640, 640), (255, 255, 255))

        # 将调整大小后的图像粘贴到新的背景上
        x_offset = (640 - resized_image.width) // 2
        y_offset = (640 - resized_image.height) // 2
        output_image.paste(resized_image, (x_offset, y_offset))

        # 保存调整大小后的图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        output_image.save(output_path)

print("已完成批量调整大小操作。")
