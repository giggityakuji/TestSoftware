import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def restart():
    os.system("sudo reboot")

def shutdown():
    os.system("sudo shutdown now")

def sleep():
    os.system("systemctl suspend")

class TitleBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.configure(bg="black")
        
        close_button = tk.Button(self, text="×", command=self.master.quit, 
                                 bg="black", fg="purple", bd=0, font=("Arial", 16))
        close_button.pack(side="right")
        
        title = tk.Label(self, text="System Control", bg="black", fg="purple", font=("Arial", 12))
        title.pack(side="left", padx=5)
        
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry(f"+{x}+{y}")

def create_gui():
    root = tk.Tk()
    root.overrideredirect(True)  # Remove default title bar
    root.geometry("300x230")
    root.configure(bg="black")

    # Set favicon
    favicon_path = 'Logo.png'  # Use the correct path to the Logo.png in the TESTFILES directory
    favicon = Image.open(favicon_path)
    favicon = ImageTk.PhotoImage(favicon)
    root.wm_iconphoto(True, favicon)

    title_bar = TitleBar(root)
    title_bar.pack(fill="x")

    content_frame = tk.Frame(root, bg="black")
    content_frame.pack(expand=True, fill="both", padx=10, pady=10)

    style = {
        "bg": "black",
        "fg": "purple",
        "font": ("Arial", 12),
        "width": 20,
        "height": 2,
        "bd": 1,  # Add a border
        "relief": "ridge"  # Give buttons a raised look
    }

    tk.Button(content_frame, text="Restart", command=restart, **style).pack(pady=5)
    tk.Button(content_frame, text="Shutdown", command=shutdown, **style).pack(pady=5)
    tk.Button(content_frame, text="Sleep", command=sleep, **style).pack(pady=5)
    tk.Button(content_frame, text="Exit", command=root.quit, **style).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
