import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import requests
from io import BytesIO
import mysql.connector
from mysql.connector import Error

class PhotoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seller Page")
        self.root.geometry("1440x1080")  # Set the root geometry to 1440x800
        self.root.minsize(1440, 800)    # Set the minimum window size
        self.root.maxsize(1440, 800)# Make the window resizable

        # Load background image
        bg_image = Image.open("Luga-Pasal\Images\sellerpage.jpg")  
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

        # Connect to MySQL database
        self.connection = self.connect_to_mysql()

        if self.connection is not None:
            self.setup_gui()
        else:
            print("Failed to establish a database connection. Check your connection details.")

    def connect_to_mysql(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="LugaPasal"
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def setup_gui(self):
    # Create and configure frame for form elements
        frame = ttk.Frame(self.root, padding="40", style="White.TFrame")  # Add style for a white background
        frame.place(relx=0.3, rely=0.6, anchor=tk.W)  # Adjusted placement for a more centered position and reduced width
        frame.columnconfigure(0, weight=1)

        # Title
        ttk.Label(frame, text="Title:").grid(column=0, row=0, sticky=tk.W)
        self.title_entry = ttk.Entry(frame, width=40)
        self.title_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=20)

        # Price
        ttk.Label(frame, text="Price(Rs):").grid(column=0, row=1, sticky=tk.W)
        self.price_entry = ttk.Entry(frame, width=40)
        self.price_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=20)

        # Description
        ttk.Label(frame, text="Description:").grid(column=0, row=2, sticky=tk.W)
        self.description_entry = tk.Text(frame, width=40, height=5, wrap=tk.WORD)
        self.description_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=20)

        # Category
        ttk.Label(frame, text="Category:").grid(column=0, row=3, sticky=tk.W)
        self.category_var = tk.StringVar()
        category_dropdown = ttk.Combobox(frame, textvariable=self.category_var,
                                         values=["Pants", "Tshirt", "Hoodie", "Jacket", "Shoes"])
        category_dropdown.grid(column=1, row=3, sticky=(tk.W, tk.E), pady=50)
        category_dropdown.set("Select Category")

        # Submit button
        submit_button = ttk.Button(frame, text="Submit", command=self.submit_form)
        submit_button.grid(column=1, row=4, sticky=(tk.W, tk.E))
        self.style_button(submit_button)  # Apply style to the button

        # Create and configure frame for photo capturing/uploading
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.place(relx=0.68, rely=0.54, anchor=tk.W)  # Updated from grid to place

        # Capture, Select, and Upload buttons for photos
        capture_btn = ttk.Button(self.root, text="Take Photo", command=self.capture_photo)
        capture_btn.place(relx=0.78, rely=0.82, anchor=tk.W)
        self.style_button(capture_btn)  # Apply style to the button
        # Update seller_btn command to open loginbuyer
        seller_btn = ttk.Button(self.root, text="Start Buying", command=self.open_loginbuyer)

        seller_btn.place(relx=0.8, rely=0.07, anchor=tk.W)
        self.style_button(seller_btn)  # Apply style to the button

        select_btn = ttk.Button(self.root, text="Select Photo", command=self.select_photo)
        select_btn.place(relx=0.78, rely=0.87, anchor=tk.W)
        self.style_button(select_btn)  # Apply style to the button

        upload_btn = ttk.Button(self.root, text="Upload Photo", command=self.upload_photo)
        upload_btn.place(relx=0.78, rely=0.92, anchor=tk.W)
        self.style_button(upload_btn)  # Apply style to the button

        # Initialize attribute to hold the captured image
        self.captured_image = None

    def style_button(self, button):
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 20))
    def open_loginbuyer(event=None):
        root.destroy()
        import loginbuyer

    def capture_photo(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.photo = photo

        self.captured_image = image

        cap.release()

    def select_photo(self):
        file_path = filedialog.askopenfilename(title="Select Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            image = Image.open(file_path)

            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.photo = photo

            self.captured_image = image

    
            messagebox.showerror("Error", "Please capture or select a photo first.")
    def upload_photo(self):
        if self.captured_image is not None:
            try:
                img_bytes = BytesIO()
                self.captured_image.save(img_bytes, format="JPEG")
                img_data = img_bytes.getvalue()

                description = self.description_entry.get("1.0", tk.END).strip()
                category = self.category_var.get()

                # Replace the URL with the actual endpoint for uploading
                upload_url = "https://example.com/upload"

                # Replace 'file', 'description', and 'category' with the field names expected by the server
                files = {'file': ('photo.jpg', img_data), 'description': description, 'category': category}

                # Make the upload request
                response = requests.post(upload_url, files=files)

                if response.status_code == 200:
                    messagebox.showinfo("Success", "Photo uploaded successfully!")
                else:
                    messagebox.showerror("Error", f"Failed to upload photo. Status code: {response.status_code}")

            except Exception as e:
                messagebox.showerror("Error", f"Error uploading photo: {e}")
        else:
            messagebox.showerror("Error", "Please capture or select a photo first.")
    
    def submit_form(self):
        title_value = self.title_entry.get()
        price_value = self.price_entry.get()
        description_value = self.description_entry.get("1.0", tk.END).strip()
        category_value = self.category_var.get()

        # Insert data into the 'product' table
        self.insert_into_product_table(title_value, price_value, description_value, category_value)

    def insert_into_product_table(self, title, price, description, category):
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO product (title, price, description, category) VALUES (%s, %s, %s, %s)"
            values = (title, price, description, category)
            cursor.execute(query, values)
            self.connection.commit()
            messagebox.showinfo("Product Successfully added")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoApp(root)
    
    
    root.mainloop()
    app.close_mysql_connection()