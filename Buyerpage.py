from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
from datetime import datetime


root=Tk()
root.title("Brocode")

root.geometry("1440x1080")

root.configure(bg="gray")

bg_image = ImageTk.PhotoImage(Image.open("Images/login.jpg"))



#creating a heading
Heading=LabelFrame(root,bd=2,relief="flat",bg="light yellow")
Heading.place(x=0,y=0,width=1440,height=55)
image_logo=ImageTk.PhotoImage(Image.open("Images/logo.png"))
heading_bg=Label(Heading, image=bg_image).place(relheight=1,relwidth=1)
name=Label(Heading,text="Luga Pasal",font=("Comic Sans MS",28,"bold"),fg="black").grid(row=0,column=1)
tagline=Label(Heading,text="Be fashionable!",font="magneto 16 italic",fg="Red").grid(row=0,column=2,padx=280)

#creating frames inside root
Products_frame=LabelFrame(root,bd=2,relief="flat",text="Products",font="arial 16 bold",fg="Red")
Products_frame.place(x=310,y=55,width=1200,height=720)


Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=0,y=55,width=310,height=380)
label_logo_button=Label(Button_frame,image=bg_image,bd=2).place(relheight=1,relwidth=1)


root.mainloop()