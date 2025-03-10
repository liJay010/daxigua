from PIL import Image, ImageDraw

def convert_to_rgba_with_inner_circle(image_path, output_path, target_size):
    # 打开图片并转换为RGBA
    img = Image.open(image_path).convert("RGBA")
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

size = 408
org_path = "./pic/" + str(size) + ".jpg"

out_path = r"E:\Desktop\blog\daxigua\res\raw-assets\50\5035266c-8df3-4236-8d82-a375e97a0d9c.png"
# 示例调用
convert_to_rgba_with_inner_circle(org_path, out_path, size)
