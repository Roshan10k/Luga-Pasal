from tkinter import *
from PIL import Image,ImageTk
from tkmacosx import Button

def open_seller_login():
    root.destroy()
    import loginseller
   

def open_buyer_login():
    root.destroy()
    import loginbuyer
  

root=Tk()
root.title("Homepage")
root.geometry("1440x1080")



bg_image=PhotoImage(file="Luga-Pasal\Images\homepage.png")
bg_label=Label(root,image=bg_image)
bg_label.place(relheight=1,relwidth=1)


font_style = ("Pacifico", 16)

Seller_button=Button(root,text="Seller",bg="Lightblue",font=font_style,relief="groove",command=open_seller_login)
Seller_button.place(x=910,y=310,height=60,width=100)

buyer_button=Button(root,text="Buyer",bg="Lightblue",font=font_style,relief="groove",command=open_buyer_login)
buyer_button.place(x=910,y=480,height=60,width=100)

root.mainloop()