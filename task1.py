import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def load_image():
    file_path = filedialog.askopenfilename(
        title="Оберіть зображення",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

def save_info():
    entered_text = input_text.get() 
    entered_format = input_format.get()
    valid_formats = ["jpg", "jpeg", "png", "bmp", "tiff"]

    if entered_text:
        if entered_format in valid_formats:
            print("Введена назва:", entered_text)
            print("Введений формат:", entered_format)   
            print("Зберігаємо картинку...")
            img_path = load_image()
            if img_path:
                img = Image.open(img_path)
                img.save(entered_text + "." + entered_format)
                window.destroy()
            else: 
                messagebox.showerror("Помилка :(", "Не вдалося обрати зображення")
        else:
            messagebox.showerror("Невірно введений формат!", "Будь ласка, введіть валідний формат!")
    else:
        messagebox.showerror("Не введено назву!", "Будь ласка, введіть назву для зберігаємої картинки.")

window = tk.Tk()
window.title("test")
window.geometry("600x400")
input_text = tk.StringVar()
input_format = tk.StringVar()

label = tk.Label(window, text="Введіть назву картинки:")
label.pack(pady=10)

entry = tk.Entry(window, textvariable=input_text)
entry.pack(pady=10)

label2 = tk.Label(window, text="Оберіть формат:")
label2.pack(pady=10)

entry2 = tk.Entry(window, textvariable=input_format)
entry2.pack(pady=10)

save_button = tk.Button(window, text="Зберегти", command=save_info)
save_button.pack(pady=10)

window.mainloop()