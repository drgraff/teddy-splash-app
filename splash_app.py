
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("Splash Screen")
    root.geometry("800x600")
    root.resizable(False, False)

    try:
        image = Image.open("splash_image.png")
        image = image.resize((800, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()
    except Exception as e:
        label = tk.Label(root, text=f"Image failed to load: {e}")
        label.pack()

    ok_button = ttk.Button(root, text="OK", command=root.destroy)
    ok_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
