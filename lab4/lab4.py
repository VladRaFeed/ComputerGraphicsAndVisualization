from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox
import numpy as np

def load_image():
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

image_path = load_image()
image = Image.open(image_path)

def task1():
    plt.figure(figsize=(6, 6))
    plt.title("Оригінальне зображення")
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def task2():

    brightness_matrix = np.dot(np.array(image)[..., :3], [0.3, 0.59, 0.11])  # Формула для яскравості

    brightness_matrix = np.round(brightness_matrix).astype(int)

    output_file = "brightness_matrix.txt"  
    np.savetxt(output_file, brightness_matrix, fmt="%d", delimiter="\t")

    print(f"Матриця яскравості збережена у файл: {output_file}")

def task3():
    colors = ('r', 'g', 'b')
    plt.figure(figsize=(8, 6))
    for i, color in enumerate(colors):
        channel_data = np.array(image)[:, :, i].flatten()
        plt.hist(channel_data, bins=256, alpha=0.5, color=color, label=f"{color.upper()} Channel")
    plt.title("Гістограма яскравості кольорового зображення")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

def task4():
    binary_image = image.convert('L').point(lambda x: 255 if x > 128 else 0, '1')
    plt.figure(figsize=(6, 6))
    plt.title("Бінаризація зображення")
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')
    plt.show()

def task5():
    grayscale_image = image.convert('L')
    plt.figure(figsize=(6, 6))
    plt.title("Перехід до відтінків сірого")
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')
    plt.show()

def task6():
    negative_image = ImageOps.invert(image.convert('RGB'))
    plt.figure(figsize=(6, 6))
    plt.title("Перехід до негативу")
    plt.imshow(negative_image)
    plt.axis('off')
    plt.show()

def task7():
    grayscale_image = image.convert('L')
    gray_values = np.array(grayscale_image).flatten()
    plt.figure(figsize=(8, 6))
    plt.hist(gray_values, bins=256, color='gray', alpha=0.7)
    plt.title("Гістрограма зображення в градаціях сірого")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()

# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()