from tkinter import *
from PIL import ImageTk, Image
from tkinter import Button



    
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



root.mainloop()
