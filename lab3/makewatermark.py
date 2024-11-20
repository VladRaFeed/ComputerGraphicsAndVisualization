from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog, messagebox

def add_watermark():
    print("Оберіть зображення")
    image_path = load_image()
    
    output_path = "watermarked_image.png"
    
    print("Введіть текст для вотермарки")
    watermark_text = input()
    
    print("Оберіть позицію вотермарки (top-left, top-right, bottom-left, bottom-right")
    position = input()

    print("Введіть прозорість від 0 до 255")
    opacity = int(input())
    print("Введіть розмір шрифту")
    font_size = int(input())
    font_color = (0, 0, 0)  # Колір у форматі RGB
    font_path = "C:/Users/vlad/Documents/GitHub/ComputerGraphicsAndVisualization/lab3/PlayfairDisplay-VariableFont_wght.ttf"
    
    image = Image.open(image_path).convert("RGBA")
    
    text_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_layer)
    
    font = ImageFont.truetype(font_path, font_size)
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    if position == "top-left":
        x, y = 10, 10
    elif position == "top-right":
        x, y = image.width - text_width - 10, 10
    elif position == "bottom-left":
        x, y = 10, image.height - text_height - 10
    elif position == "bottom-right":
        x, y = image.width - text_width - 10, image.height - text_height - 10
    else:
        print("Неправильна позиція. Використовуйте: top-left, top-right, bottom-left, bottom-right.")
        return
    
    draw.text((x, y), watermark_text, font=font, fill=font_color + (opacity,))
    
    watermarked_image = Image.alpha_composite(image, text_layer)
    
    watermarked_image.convert("RGB").save(output_path, "PNG")
    print(f"Зображення з водяним знаком збережено за адресою: {output_path}")


def load_image():
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

add_watermark()