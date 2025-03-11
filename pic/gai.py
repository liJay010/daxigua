from PIL import Image, ImageDraw
import os
def convert_to_rgba_with_inner_circle(image_path, output_path, target_size):
    # 打开图片并转换为RGBA
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    short_edge = min(width, height)
    
    left = (width - short_edge) // 2
    top = (height - short_edge) // 2
    right = left + short_edge
    bottom = top + short_edge

    img = img.crop((left, top, right, bottom))
    size = img.size[0]  # 正方形图片，获取宽高（相等）

    # 创建一个相同大小的透明背景
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)

    # 画内切圆（白色255表示可见，外部0表示透明）
    draw.ellipse((0, 0, size, size), fill=255)

    # 创建一个新的空白图像，白色背景，透明度0
    new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))

    # 仅保留圆内像素
    new_img.paste(img, (0, 0), mask)

    # 调整尺寸
    new_img = new_img.resize((target_size, target_size), Image.ANTIALIAS)

    # 保存输出图片
    new_img.save(output_path, format="PNG")



with open("path.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split()  # 去除换行符并按空格分割
        
        size = int(parts[0])
        org_path = "./pic/" + parts[0] + ".png"
        if not os.path.exists(org_path):
            org_path = "./pic/" + parts[0] + ".jpg"
        convert_to_rgba_with_inner_circle(org_path, parts[1], size)

out_path = org_path
# 示例调用
#convert_to_rgba_with_inner_circle(org_path, out_path, size)


