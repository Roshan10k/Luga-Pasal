from tkinter import *
from PIL import ImageTk, Image
from tkmacosx import Button
import mysql.connector




def toggle_password(password_entry, confirm_password_entry, toggle_button):
    current_state = password_entry["show"]
    new_state = "" if current_state else "*"
    password_entry["show"] = new_state
    confirm_password_entry["show"] = new_state

    # Toggle the button icon
    icon = eye_show_icon if current_state else eye_hide_icon
    toggle_button.configure(image=icon)
def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        login_result_label.config(text="Please fill in all the fields", fg="red")
        return

    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="LugaPasal"
        )

        cursor = conn.cursor()

        # Executing a query to check if the username and password match any records in the 'buyer' table
        cursor.execute("SELECT * FROM Seller WHERE username=%s AND password=%s", (username, password))
        user_data = cursor.fetchone()

        conn.close()

        if user_data:
            root.destroy()
            import Sellerpage
            Sellerpage.open()
           
        else:
            login_result_label.config(text="Invalid username or password", fg="red")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        login_result_label.config(text="Database error", fg="red")

def register_user():
  root.destroy()
  import registerseller
  registerseller.open()


root=Tk()
root.title("Seller Login Form")
root.geometry("1440x1080")

# Background image
bg_image = PhotoImage(file="Images/loginseller.png")  
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Variables
show_password_var = BooleanVar()

font_style = ("Pacifico", 16)

login_frame = LabelFrame(root, bg="white", font=font_style, relief="flat")
login_frame.place(x=500, y=350, width=450, height=350)

# Username entry for login
Label(login_frame, text="Username", bg="white", font=font_style).grid(row=0, column=0, padx=10, pady=10, sticky="w" )
login_username_entry = Entry(login_frame, font=font_style, width=30)
login_username_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="w")

# Password entry for login
Label(login_frame, text="Password", bg="white", font=font_style).grid(row=2, column=0, padx=10, pady=10, sticky="w" )
login_password_entry = Entry(login_frame, show="*", font=font_style, width=30)
login_password_entry.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Toggle Password button for Login Password entry
eye_show_icon = PhotoImage(file="Images/eye_open.png") 
eye_hide_icon = PhotoImage(file="Images/eye-close.png") 
toggle_button_login_password = Button(login_frame, command=lambda: toggle_password(login_password_entry, None, toggle_button_login_password), image=eye_show_icon, bg="white")
toggle_button_login_password.grid(row=3, column=2, pady=10)

login_button = Button(login_frame, text="Login", bg="Green", padx=5, pady=2, font=font_style,command=login_user)
login_button.grid(row=4, column=0, pady=10, columnspan=3)

login_result_label = Label(login_frame, text="", bg="white", font=font_style)
login_result_label.grid(row=6, column=0, columnspan=1, pady=10)

label_register=Label(login_frame,text="Do you have an account?",bg="white",font=font_style)
label_register.grid(row=5,column=0)

register_button=Button(login_frame,text="Register",bg="lightblue",padx=5,pady=2,font=font_style,command=register_user)
register_button.grid(row=5,column=1,pady=10,columnspan=3)

root.mainloop()

