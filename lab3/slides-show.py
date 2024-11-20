import os
import tkinter as tk
from PIL import Image, ImageTk

def create_slideshow():
    folder_path = "C:/Users/vlad/Documents/GitHub/ComputerGraphicsAndVisualization/lab3/images"  # Папка зі зображеннями
    print("Введіть затримку для слайд шоу")
    delay = int(input())
    
    image_files = [file for file in os.listdir(folder_path)]
    
    root = tk.Tk()
    root.title("Слайд-шоу")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    frame = tk.Frame(root, bg="black")
    frame.pack(fill=tk.BOTH, expand=True)
    
    label = tk.Label(frame, bg="black")
    label.pack(expand=True)
    
    current_index = [0]
    
    def show_next_image():
        image_path = os.path.join(folder_path, image_files[current_index[0]])
        image = Image.open(image_path)
        
        image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        
        label.config(image=photo)
        label.image = photo
        
        current_index[0] = (current_index[0] + 1) % len(image_files)
        
        root.after(delay, show_next_image)
    
    show_next_image()
    
    root.mainloop()

create_slideshow()