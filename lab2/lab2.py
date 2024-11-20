import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance

def show_change_alpha_pixel_to_setted():
    clear_frame()

    def changecolors():
        entered_alpha = input_a.get()  
        
        img_path = load_image()
        if img_path:
            img = Image.open(img_path).convert("RGBA")  
            width, height = img.size
            pixels = img.load()
            for i in range(width):
                for j in range(height):
                    r, g, b, a = pixels[i, j]  
                    a = int(a * entered_alpha)  
                    pixels[i, j] = (r, g, b, a)  
            img.save("repainted_image.png")  
        else:
            messagebox.showerror("Помилка!", "Не вдається відкрити зображення")

    input_a = tk.DoubleVar()  

    label = tk.Label(frame, text="Введіть альфу, для зміни прозорості (0.1-0.9):")
    label.pack(pady=10)

    entry1 = tk.Entry(frame, textvariable=input_a)
    entry1.pack(pady=10)

    save_button = tk.Button(frame, text="Замінити кольори", command=changecolors)
    save_button.pack(pady=10)

def show_split_image_on_parts():
    clear_frame()

    def process_image(fill_color=(0, 0, 0)):

        action = clicked.get()
        rows = input_rows.get()
        columns = input_columns.get()
        x1 = input_x1.get()
        x2 = input_x2.get()
        y1 = input_y1.get()
        y2 = input_y2.get()

        img_path = load_image()
        image = Image.open(img_path)

        if action == 'split':
            img_width, img_height = image.size
            part_width = img_width // columns
            part_height = img_height // rows
            parts = []
            for i in range(rows):
                for j in range(columns):
                    left = j * part_width
                    upper = i * part_height
                    right = (j + 1) * part_width
                    lower = (i + 1) * part_height
                    part = image.crop((left, upper, right, lower))
                    parts.append(part)
            
            for i in range(len(parts)):
                parts[i].show()  
    
        elif action == 'extract':
            selected_region = image.crop((x1, y1, x2, y2))
            selected_region.save("selected_region.png")
            selected_region.show() 
    
        elif action == 'mask_outside':

            mask = image.copy()
            
            for x in range(x1, x2):
                for y in range(y1, y2):
                    mask.putpixel((x, y), fill_color)  # Чорний колір

            mask.show()
    
        else:
            messagebox.showerror("Некоректна дія. Використовуйте 'split', 'extract' або 'mask_outside'.")
 
    options = [ 
        "split", 
        "extract", 
        "mask_outside"
    ] 
  
    clicked = tk.StringVar() 
  
    clicked.set( "split" ) 
    
    drop = tk.OptionMenu(frame , clicked , *options ) 
    drop.pack(pady=10) 

    input_rows = tk.IntVar()
    input_columns = tk.IntVar()
    input_x1 = tk.IntVar()
    input_x2 = tk.IntVar()
    input_y1 = tk.IntVar()
    input_y2 = tk.IntVar()

    label = tk.Label(frame, text="Введіть кільіксть стовпців та рядків:")
    label.pack(pady=10)

    entry2 = tk.Entry(frame, textvariable=input_columns)
    entry2.pack(pady=10)
    entry3 = tk.Entry(frame, textvariable=input_rows)
    entry3.pack(pady=10)

    label2 = tk.Label(frame, text="Введіть координати")
    label2.pack(pady=10)

    entry4 = tk.Entry(frame, textvariable=input_x1)
    entry4.pack(pady=10)
    entry5 = tk.Entry(frame, textvariable=input_x2)
    entry5.pack(pady=10)
    entry6 = tk.Entry(frame, textvariable=input_y1)
    entry6.pack(pady=10)
    entry7 = tk.Entry(frame, textvariable=input_y2)
    entry7.pack(pady=10)

    save_button = tk.Button(frame, text="Замінити", command=process_image)
    save_button.pack(pady=10)

def show_change_contrast():
    clear_frame()

    def change_contrast():
        contrast = input_contrast.get()

        img_path = load_image()
        image = Image.open(img_path)

        if(img_path):
            enhanc = ImageEnhance.Contrast(image)
            changedContrastImage = enhanc.enhance(contrast)
            changedContrastImage.show()
        else: 
            messagebox.showerror("Виберіть коректне зображення!")

    input_contrast = tk.IntVar()

    label = tk.Label(frame, text="Введіть значення для зміни контрасту:")
    label.pack(pady=10)

    entry1 = tk.Entry(frame, textvariable=input_contrast)
    entry1.pack(pady=10)

    save_button = tk.Button(frame, text="Змінити контраст", command=change_contrast)
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

btn_changecolors = tk.Button(root, text="Зміна прозорості", command=show_change_alpha_pixel_to_setted)
btn_changecolors.pack(pady=10)

btn_deletearea = tk.Button(root, text="Видалити шматок фото", command=show_split_image_on_parts)
btn_deletearea.pack(pady=10)

btn_deletearea = tk.Button(root, text="Змінити контраст фото", command=show_change_contrast)
btn_deletearea.pack(pady=10)

root.geometry("600x600")
root.mainloop()