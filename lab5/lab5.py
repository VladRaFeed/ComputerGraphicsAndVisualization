from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np

def load_image():
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

def apply_filter():
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixels = np.array(image)

    window_size = 5 # розмір вікна
    padding = window_size // 2

    new_pixels = np.copy(pixels)

    # Проходимо по кожному пікселю зображення (крім межових)
    for i in range(padding, pixels.shape[0] - padding):
        for j in range(padding, pixels.shape[1] - padding):
            # Відбираємо пікселі у межах ковзного вікна
            window = pixels[i-padding:i+padding+1, j-padding:j+padding+1]

            # Обчислюємо середнє значення пікселів у вікні для кожного каналу (R, G, B)
            avg_color = np.mean(window, axis=(0, 1))

            new_pixels[i, j] = avg_color

    filtered_image = Image.fromarray(new_pixels)
    filtered_image_tk = ImageTk.PhotoImage(filtered_image)
    panel.config(image=filtered_image_tk)
    panel.image = filtered_image_tk

root = Tk()
root.title("Фільтрація зображення")
image_path = load_image()
if image_path:
    image = Image.open(image_path)
    image_tk = ImageTk.PhotoImage(image)
    panel = Label(root, image=image_tk)
    panel.pack()
    button = Button(root, text="Застосувати фільтрацію", command=apply_filter)
    button.pack()

root.mainloop()
