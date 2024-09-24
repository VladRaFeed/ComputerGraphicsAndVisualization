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

        if(entered_width or entered_height != 0):
            img_path = load_image()
            if img_path:
                img = Image.open(img_path)
                width, height = img.size
                if(entered_height or entered_width == 0):
                    if(entered_height == 0):
                        a = width / height
                        new_height = entered_width / a
                        new_width = a * new_height
                    else: 
                        a = width / height
                        new_width = entered_height * a
                        new_height = new_width / a
                    a = width / height
                    new_height = entered_width / a
                    new_width = a * new_height
                resized_img = img.resize((int(new_width), int(new_height)))
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

def show_change_select_pixel_to_setted_color():
    clear_frame()

    def changecolors():
        entered_color1R = input_R1.get()
        entered_color2R = input_R2.get()
        entered_color1G = input_G1.get()
        entered_color2G = input_G2.get()
        entered_color1B = input_B1.get()
        entered_color2B = input_B2.get()
        
        img_path = load_image()
        if img_path:
            img = Image.open(img_path)
            width, height = img.size
            pixels = img.load()
            for i in range(width):
                for j in range(height):
                    if pixels[i, j] == (entered_color1R, entered_color1G, entered_color1B):
                        pixels[i,j] = (entered_color2R, entered_color2G, entered_color2B)
            img.save("repainted_image.jpg")
        else:
            messagebox.showerror("Помилка!", "Не вдається відкрити зображення")

    input_R1 = tk.IntVar()
    input_G1 = tk.IntVar()
    input_B1 = tk.IntVar()
    input_R2 = tk.IntVar()
    input_G2 = tk.IntVar()
    input_B2 = tk.IntVar()
    
    label = tk.Label(frame, text="Введіть колір, який ви хочете обрати для заміни:")
    label.pack(pady=10)

    entry1 = tk.Entry(frame, textvariable=input_R1)
    entry1.pack(pady=10)
    entry2 = tk.Entry(frame, textvariable=input_G1)
    entry2.pack(pady=10)
    entry3 = tk.Entry(frame, textvariable=input_B1)
    entry3.pack(pady=10)

    label2 = tk.Label(frame, text="Введіть колір на який ви хочете замінити обраний колір")
    label2.pack(pady=10)

    entry4 = tk.Entry(frame, textvariable=input_R2)
    entry4.pack(pady=10)
    entry5 = tk.Entry(frame, textvariable=input_G2)
    entry5.pack(pady=10)
    entry6 = tk.Entry(frame, textvariable=input_B2)
    entry6.pack(pady=10)

    save_button = tk.Button(frame, text="Замінити кольори", command=changecolors)
    save_button.pack(pady=10)

def show_change_color_scale():
    clear_frame()

    def colorscale():
        entered_R = float(input_Rscale.get())
        entered_G = float(input_Gscale.get())
        entered_B = float(input_Bscale.get())

        img_path = load_image()
        if img_path:
            img = Image.open(img_path)
            width, height = img.size
            pixels = img.load()
            for i in range(width):
                for j in range(height):
                    color = pixels[i, j]
                    new_color = (int(color[0] * entered_R), int(color[1] * entered_G), int(color[2] * entered_B))
                    pixels[i, j] = new_color
            img.save("changed_scale_image.jpg")
        else:
            messagebox.showerror("Помилка!", "Не вдається відкрити зображення")

    
    input_Rscale = tk.StringVar()
    input_Gscale = tk.StringVar()
    input_Bscale = tk.StringVar()

    labelR=tk.Label(frame, text="Введіть значення для R")
    labelR.pack(pady=10)

    entryR = tk.Entry(frame, textvariable=input_Rscale)
    entryR.pack(pady=10)

    labelG=tk.Label(frame, text="Введіть значення для G")
    labelG.pack(pady=10)

    entryG = tk.Entry(frame, textvariable= input_Gscale)
    entryG.pack(pady=10)

    labelB=tk.Label(frame, text="Введіть значення для B")
    labelB.pack(pady=10)

    entryB = tk.Entry(frame, textvariable=input_Bscale)
    entryB.pack(pady=10)

    save_button = tk.Button(frame, text="Змінити кольори", command=colorscale)
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
btn_format.pack(pady=10)

btn_resize = tk.Button(root, text="Зміна розміру зображення", command=show_resize)
btn_resize.pack(pady=10)

btn_changecolors = tk.Button(root, text="Зміна кольору на заданий", command=show_change_select_pixel_to_setted_color)
btn_changecolors.pack(pady=10)

btn_changecolorsacle = tk.Button(root, text="Корекція колірного балансу", command=show_change_color_scale)
btn_changecolorsacle.pack(pady=10)

root.geometry("600x600")
root.mainloop()