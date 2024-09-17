import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


#change format func
def show_change_format():
    clear_frame()

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
                else: 
                    messagebox.showerror("Помилка :(", "Не вдалося обрати зображення")
            else:
                messagebox.showerror("Невірно введений формат!", "Будь ласка, введіть валідний формат!")
        else:
            messagebox.showerror("Не введено назву!", "Будь ласка, введіть назву для зберігаємої картинки.")

    input_text = tk.StringVar()
    input_format = tk.StringVar()
    
    label = tk.Label(frame, text="Введіть назву картинки:")
    label.pack(pady=10)
    
    entry = tk.Entry(frame, textvariable=input_text)
    entry.pack(pady=10)
    
    label2 = tk.Label(frame, text="Оберіть формат:")
    label2.pack(pady=10)
    
    entry2 = tk.Entry(frame, textvariable=input_format)
    entry2.pack(pady=10)
    
    save_button = tk.Button(frame, text="Зберегти", command=save_info)
    save_button.pack(pady=10)

def show_resize():
    clear_frame()

    def resize():
        entered_width = int(input_width.get())
        entered_height = int(input_height.get())

        if(entered_width & entered_height != 0):
            img_path = load_image()
            if img_path:
                img = Image.open(img_path)
                resized_img = img.resize((entered_width, entered_height))
                resized_img.save("resized_img.jpg")
                resized_img.show()
            else: 
                messagebox.showerror("Помилка!", "Не вдалося обрати зображення")
        else:
            messagebox.showerror("Помилка!", "Введіть значення відмінні від нуля")

    input_width = tk.IntVar()
    input_height = tk.IntVar()

    label = tk.Label(frame, text="Введіть ширину:")
    label.pack(pady=10)

    entry = tk.Entry(frame, textvariable=input_width)
    entry.pack(pady=10)

    label2 = tk.Label(frame, text="Введіть висоту:")
    label2.pack(pady=10)

    entry2 = tk.Entry(frame, textvariable=input_height)
    entry2.pack(pady=10)

    save_button = tk.Button(frame, text="Змінити розмір", command=resize)
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

btn_format = tk.Button(root, text="Зміна формату зображення", command=show_change_format)
btn_format.pack(side=tk.LEFT, padx=10, pady=10)

btn_resize = tk.Button(root, text="Зміна розміру зображення", command=show_resize)
btn_resize.pack(side=tk.LEFT, padx=10, pady=10)

root.geometry("600x400")
root.mainloop()