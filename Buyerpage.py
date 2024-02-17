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

pants1_image=ImageTk.PhotoImage(Image.open("Images/pants1.jpeg"))
pants2_image=ImageTk.PhotoImage(Image.open("Images/pants2.jpg"))
pants3_image=ImageTk.PhotoImage(Image.open("Images/pants3.jpeg"))
pants4_image=ImageTk.PhotoImage(Image.open("Images/pants4.jpeg"))
pants5_image=ImageTk.PhotoImage(Image.open("Images/pants5.webp"))
pants6_image=ImageTk.PhotoImage(Image.open("Images/pants6.webp"))
pants7_image=ImageTk.PhotoImage(Image.open("Images/pants7.webp"))
pants8_image=ImageTk.PhotoImage(Image.open("Images/pants8.jpg"))
pants9_image=ImageTk.PhotoImage(Image.open("Images/pants9.jpg"))
pants10_image=ImageTk.PhotoImage(Image.open("Images/pants10.jpeg"))
Tshirt1_image=ImageTk.PhotoImage(Image.open("Images/Tshirt1.jpeg"))
Tshirt2_image=ImageTk.PhotoImage(Image.open("Images/Tshirt2.jpeg"))
Tshirt3_image=ImageTk.PhotoImage(Image.open("Images/Tshirt3.jpeg"))
Tshirt4_image=ImageTk.PhotoImage(Image.open("Images/Tshirt4.jpeg"))
Tshirt5_image=ImageTk.PhotoImage(Image.open("Images/Tshirt5.jpeg"))
Tshirt6_image=ImageTk.PhotoImage(Image.open("Images/Tshirt6.jpeg"))
Tshirt7_image=ImageTk.PhotoImage(Image.open("Images/Tshirt7.jpeg"))
Tshirt8_image=ImageTk.PhotoImage(Image.open("Images/Tshirt8.jpeg"))
Tshirt9_image=ImageTk.PhotoImage(Image.open("Images/Tshirt9.jpeg"))
Tshirt10_image=ImageTk.PhotoImage(Image.open("Images/Tshirt10.jpeg"))
shoes1_image=ImageTk.PhotoImage(Image.open("Images/shoes1.jpg"))
shoes2_image=ImageTk.PhotoImage(Image.open("Images/shoes2.jpg"))
shoes3_image=ImageTk.PhotoImage(Image.open("Images/shoes3.jpg"))
shoes4_image=ImageTk.PhotoImage(Image.open("Images/shoes4.jpg"))
shoes5_image=ImageTk.PhotoImage(Image.open("Images/shoes5.jpg"))
shoes6_image=ImageTk.PhotoImage(Image.open("Images/shoes6.jpg"))
shoes7_image=ImageTk.PhotoImage(Image.open("Images/shoes7.jpg"))
shoes8_image=ImageTk.PhotoImage(Image.open("Images/shoes8.jpg"))
shoes9_image=ImageTk.PhotoImage(Image.open("Images/shoes9.jpg"))
shoes10_image=ImageTk.PhotoImage(Image.open("Images/shoes10.jpg"))
Hoodie1_image=ImageTk.PhotoImage(Image.open("Images/Hoodie1.jpg"))
Hoodie2_image=ImageTk.PhotoImage(Image.open("Images/Hoodie2.jpg"))
Hoodie3_image=ImageTk.PhotoImage(Image.open("Images/Hoodie3.jpg"))
Hoodie4_image=ImageTk.PhotoImage(Image.open("Images/Hoodie4.jpg"))
Hoodie5_image=ImageTk.PhotoImage(Image.open("Images/Hoodie5.jpg"))
Hoodie6_image=ImageTk.PhotoImage(Image.open("Images/Hoodie6.jpg"))
Hoodie7_image=ImageTk.PhotoImage(Image.open("Images/Hoodie7.jpg"))
Hoodie8_image=ImageTk.PhotoImage(Image.open("Images/Hoodie8.jpg"))
Hoodie9_image=ImageTk.PhotoImage(Image.open("Images/Hoodie9.jpg"))
Hoodie10_image=ImageTk.PhotoImage(Image.open("Images/Hoodie10.jpg"))
Jacket1_image=ImageTk.PhotoImage(Image.open("Images/Jacket1.jpg"))
Jacket2_image=ImageTk.PhotoImage(Image.open("Images/Jacket2.jpg"))
Jacket3_image=ImageTk.PhotoImage(Image.open("Images/Jacket3.jpg"))
Jacket4_image=ImageTk.PhotoImage(Image.open("Images/Jacket4.jpg"))
Jacket5_image=ImageTk.PhotoImage(Image.open("Images/Jacket5.jpg"))
Jacket6_image=ImageTk.PhotoImage(Image.open("Images/Jacket6.jpg"))
Jacket7_image=ImageTk.PhotoImage(Image.open("Images/Jacket7.jpg"))
Jacket8_image=ImageTk.PhotoImage(Image.open("Images/Jacket8.jpg"))
Jacket9_image=ImageTk.PhotoImage(Image.open("Images/Jacket9.jpg"))
Jacket10_image=ImageTk.PhotoImage(Image.open("Images/Jacket10.jpg"))


root.mainloop()