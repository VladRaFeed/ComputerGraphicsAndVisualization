import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def merge_images():

    print("Оберіть перше зображення:")
    img_path1 = load_image()
    img1 = Image.open(img_path1)
    print("Оберіть друге зображення:")
    img_path2 = load_image()
    img2 = Image.open(img_path2)
    print("Оберіть варіант об'єднання: Горизонтально чи Вертикально")
    direction = input()
    
    if direction == 'horizontal':
        new_width = img1.width + img2.width
        new_height = max(img1.height, img2.height)
        merged_image = Image.new('RGB', (new_width, new_height))
        merged_image.paste(img1, (0, 0))
        merged_image.paste(img2, (img1.width, 0))
    elif direction == 'vertical':
        new_width = max(img1.width, img2.width)
        new_height = img1.height + img2.height
        merged_image = Image.new('RGB', (new_width, new_height))
        merged_image.paste(img1, (0, 0))
        merged_image.paste(img2, (0, img1.height))
    else:
        raise ValueError("Напрямок має бути 'horizontal' або 'vertical'.")
    
    merged_image.show()

def load_image():
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

merge_images()