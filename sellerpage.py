import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import requests
from io import BytesIO

class PhotoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seller Page")
        self.root.geometry("1440x800")  # Set the root geometry to 1440x800
        self.root.minsize(1440, 800)    # Set the minimum window size
        self.root.maxsize(1440, 800)# Make the window resizable

        # Load background image
        bg_image = Image.open("Images\sellerpage.jpg")  
        self. background = ImageTk.PhotoImage(bg_image)

        # Create a label for the background
        self.bg_label = ttk.Label(self.root, image=self.background)
        self.bg_label.place(relwidth=1, relheight=1)

        # Initialize attributes for form elements
        self.title_entry = None
        self.price_entry = None
        self.description_entry = None
        self.category_var = None

        # Initialize attributes for photo capturing/uploading
        self.canvas = None
        self.captured_image = None

        self.setup_gui()

    def setup_gui(self):
        # Create and configure frame for form elements
        frame = ttk.Frame(self.root, padding="40")  # Increased padding for a larger frame
        frame.place(relx=0.325, rely=0.6, anchor=tk.W)  # Adjusted placement for a more centered position
        frame.columnconfigure(0, weight=1)

        

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    root.mainloop()
