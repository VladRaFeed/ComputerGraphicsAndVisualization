import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def show_change_select_pixel_to_setted_color():
    clear_frame()

    def changecolors():
        entered_alpha = input_a.get()  # Використовуйте введене значення прямо
        
        img_path = load_image()
        if img_path:
            img = Image.open(img_path).convert("RGBA")  # Конвертуємо в RGBA
            width, height = img.size
            pixels = img.load()
            for i in range(width):
                for j in range(height):
                    r, g, b, a = pixels[i, j]  # Отримуємо значення кольору та альфа
                    a = int(a * entered_alpha)  # Змінюємо альфа-канал
                    # a = max(0, min(255, a))  # Переконайтеся, що значення альфа в діапазоні 0-255
                    pixels[i, j] = (r, g, b, a)  # Зберігаємо нові значення пікселя
            img.save("repainted_image.png")  # Зберігаємо в PNG для збереження альфа-каналу
        else:
            messagebox.showerror("Помилка!", "Не вдається відкрити зображення")

    input_a = tk.DoubleVar()  # Використовуйте DoubleVar для значень з плаваючою крапкою

    label = tk.Label(frame, text="Введіть альфу, для зміни прозорості (0.1-0.9):")
    label.pack(pady=10)

    entry1 = tk.Entry(frame, textvariable=input_a)
    entry1.pack(pady=10)

    save_button = tk.Button(frame, text="Замінити кольори", command=changecolors)
    save_button.pack(pady=10)

def load_image():
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

#main window
root = tk.Tk()
root.title("Робота з зображеннями")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

btn_changecolors = tk.Button(root, text="Зміна прозорості", command=show_change_select_pixel_to_setted_color)
btn_changecolors.pack(pady=10)

root.geometry("600x600")
root.mainloop()