from tkinter import *
from PIL import ImageTk, Image
from tkinter import Button

def toggle_password(password_entry, confirm_password_entry, toggle_button):
    current_state = password_entry["show"]
    new_state = "" if current_state else "*"
    password_entry["show"] = new_state
    confirm_password_entry["show"] = new_state

    # Toggle the button icon
    icon = eye_show_icon if current_state else eye_hide_icon
    toggle_button.configure(image=icon)

def register_user():
    username = username_entry.get()
    full_name = full_name_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not full_name or not password or not confirm_password:
        result_label.config(text="Sabai haal muji", fg="red")
    elif password != confirm_password:
        result_label.config(text="Passwords do not match", fg="red")
    else:
        result_label.config(text=f"Registration successful!", fg="green")

    
# def go_back():
#     root.destroy()
#     import loginbuyer
#     loginbuyer.go_back()
    

# Main window
root = Tk()
root.title("Registration Form")
root.geometry("1440x1080")

# Background image
bg_image = PhotoImage(file="Luga-Pasal\Images\signup.png")  
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Variables
show_password_var = BooleanVar()

font_style = ("Pacifico", 16)

register_frame = LabelFrame(root, bg="white", font=font_style)
register_frame.place(x=750, y=160, width=450, height=500)

point_image = ImageTk.PhotoImage(Image.open("Luga-Pasal\Images\pointw.webp"))  
point_label = Label(register_frame, image=point_image, borderwidth=0, highlightthickness=0)
point_label.place(x=250, y=0)

# Full Name entry
Label(register_frame, text="Full Name:", bg="white", font=font_style).grid(row=0, column=0, padx=10, pady=10, sticky="w")
full_name_entry = Entry(register_frame, font=font_style)
full_name_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=3,sticky="w")

# Username entry
Label(register_frame, text="Username:", bg="white", font=font_style).grid(row=2, column=0, padx=10, pady=10, sticky="w" )
username_entry = Entry(register_frame, font=font_style)
username_entry.grid(row=3, column=0, padx=10, pady=10, columnspan=3,sticky="w")

# Password entry
Label(register_frame, text="Password:", bg="white", font=font_style).grid(row=4, column=0, padx=10, pady=10, sticky="w" )
password_entry = Entry(register_frame, show="*", font=font_style)
password_entry.grid(row=5, column=0, padx=10, pady=10, columnspan=2,sticky="w")

# Toggle Password button for Password entry
eye_show_icon = PhotoImage(file="Luga-Pasal\Images\eye_open.png")  
eye_hide_icon = PhotoImage(file="Luga-Pasal\Images\eye-close.png") 
toggle_button_password = Button(register_frame, command=lambda: toggle_password(password_entry, confirm_password_entry, toggle_button_password), image=eye_show_icon, bg="white")
toggle_button_password.grid(row=5, column=2, pady=10)

# Confirm Password entry
Label(register_frame, text="Confirm Password:", bg="white", font=font_style).grid(row=6, column=0, padx=10, pady=10, sticky="w" )
confirm_password_entry = Entry(register_frame, show="*", font=font_style)
confirm_password_entry.grid(row=7, column=0, padx=10, pady=10, columnspan=2,sticky="w")

# Toggle Password button for Confirm Password entry
toggle_button_confirm_password = Button(register_frame, command=lambda: toggle_password(password_entry, confirm_password_entry, toggle_button_confirm_password), image=eye_show_icon, bg="white")
toggle_button_confirm_password.grid(row=7, column=2, pady=10)

register_button = Button(register_frame, text="Register", bg="green", command=register_user, padx=5, pady=2, font=font_style)
register_button.grid(row=8, column=0, pady=10, columnspan=3)

result_label = Label(register_frame, text="", bg="white", font=font_style)
result_label.grid(row=9, column=0, columnspan=3, pady=10)

#creating go back to login button 
goback_button=Button(register_frame,text="Return Back",padx=5,pady=2,font=font_style)
goback_button.grid(row=9, column=3,pady=10)


root.mainloop()
