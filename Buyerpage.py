from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkmacosx import Button
from datetime import datetime


root=Tk()
root.title("Brocode")

root.geometry("1440x1080")

root.configure(bg="gray")

frame_image=ImageTk.PhotoImage(Image.open("Images/login.jpg"))

# Background image
bg_image = PhotoImage(file="Images/mainpage.png")  
bg_label = Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

#Productframe Image
productframe_image=ImageTk.PhotoImage(Image.open("Luga-Pasal\Images\PRODUCTFRAME.jpg"))

#creating frames inside root
Products_frame=LabelFrame(root,bd=2,relief="flat",text="Products",font="arial 16 bold",fg="Red")
Products_frame.place(x=310,y=80,width=1200,height=720)
productframe_bg=Label(Products_frame,image=productframe_image)
productframe_bg.place(relheight=1,relwidth=1)

Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=0,y=80,width=310,height=350)
label_logo_button=Label(Button_frame,image=frame_image,bd=2).place(relheight=1,relwidth=1)



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

#pants Variables
clicked_pants1=StringVar()
clicked_pants1.set("Size")
clicked_pants2=StringVar()
clicked_pants2.set("Size")
clicked_pants3=StringVar()
clicked_pants3.set("Size")
clicked_pants4=StringVar()
clicked_pants4.set("Size")
clicked_pants5=StringVar()
clicked_pants5.set("Size")
clicked_pants6=StringVar()
clicked_pants6.set("Size")
clicked_pants7=StringVar()
clicked_pants7.set("Size")
clicked_pants8=StringVar()
clicked_pants8.set("Size")
clicked_pants9=StringVar()
clicked_pants9.set("Size")
clicked_pants10=StringVar()
clicked_pants10.set("Size")
pants_list=[]

#Tshirt Variables
clicked_Tshirt1=StringVar()
clicked_Tshirt1.set("Size")
clicked_Tshirt2=StringVar()
clicked_Tshirt2.set("Size")
clicked_Tshirt3=StringVar()
clicked_Tshirt3.set("Size")
clicked_Tshirt4=StringVar()
clicked_Tshirt4.set("Size")
clicked_Tshirt5=StringVar()
clicked_Tshirt5.set("Size")
clicked_Tshirt6=StringVar()
clicked_Tshirt6.set("Size")
clicked_Tshirt7=StringVar()
clicked_Tshirt7.set("Size")
clicked_Tshirt8=StringVar()
clicked_Tshirt8.set("Size")
clicked_Tshirt9=StringVar()
clicked_Tshirt9.set("Size")
clicked_Tshirt10=StringVar()
clicked_Tshirt10.set("Size")
Tshirt_list=[]

#Shoes variables
clicked_shoes1=StringVar()
clicked_shoes1.set("Size")
clicked_shoes2=StringVar()
clicked_shoes2.set("Size")
clicked_shoes3=StringVar()
clicked_shoes3.set("Size")
clicked_shoes4=StringVar()
clicked_shoes4.set("Size")
clicked_shoes5=StringVar()
clicked_shoes5.set("Size")
clicked_shoes6=StringVar()
clicked_shoes6.set("Size")
clicked_shoes7=StringVar()
clicked_shoes7.set("Size")
clicked_shoes8=StringVar()
clicked_shoes8.set("Size")
clicked_shoes9=StringVar()
clicked_shoes9.set("Size")
clicked_shoes10=StringVar()
clicked_shoes10.set("Size")
shoes_list=[]

#Hoodie variables
clicked_Hoodie1=StringVar()
clicked_Hoodie1.set("Size")
clicked_Hoodie2=StringVar()
clicked_Hoodie2.set("Size")
clicked_Hoodie3=StringVar()
clicked_Hoodie3.set("Size")
clicked_Hoodie4=StringVar()
clicked_Hoodie4.set("Size")
clicked_Hoodie5=StringVar()
clicked_Hoodie5.set("Size")
clicked_Hoodie6=StringVar()
clicked_Hoodie6.set("Size")
clicked_Hoodie7=StringVar()
clicked_Hoodie7.set("Size")
clicked_Hoodie8=StringVar()
clicked_Hoodie8.set("Size")
clicked_Hoodie9=StringVar()
clicked_Hoodie9.set("Size")
clicked_Hoodie10=StringVar()
clicked_Hoodie10.set("Size")

Hoodie_list=[]


#Jacket variables
clicked_Jacket1=StringVar()
clicked_Jacket1.set("Size")
clicked_Jacket2=StringVar()
clicked_Jacket2.set("Size")
clicked_Jacket3=StringVar()
clicked_Jacket3.set("Size")
clicked_Jacket4=StringVar()
clicked_Jacket4.set("Size")
clicked_Jacket5=StringVar()
clicked_Jacket5.set("Size")
clicked_Jacket6=StringVar()
clicked_Jacket6.set("Size")
clicked_Jacket7=StringVar()
clicked_Jacket7.set("Size")
clicked_Jacket8=StringVar()
clicked_Jacket8.set("Size")
clicked_Jacket9=StringVar()
clicked_Jacket9.set("Size")
clicked_Jacket10=StringVar()
clicked_Jacket10.set("Size")

Jacket_list=[]


#defining function to hide all frames inside product frame
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()

# defining space function to create spaces where needed
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s
#defining function for save invoice
def save_invoice(text):
    op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=open("Invoices/"+s+".doc","w")
        f.write(text)
        f.close()
        messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
    else:
        messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
#defining pants and its attributes
def pantsCall():
   
    HideAllFrames()
   
    pants_Label=Label(Products_frame,text="Pants",font="times 18 bold",fg="red").grid(row=0,column=0,padx=20)
    lf_pants1=LabelFrame(Products_frame,bd=2,relief="flat",borderwidth=0)
    lf_pants1.place(x=20,y=55,width=180,height=300)
    lf_pants2=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants2.place(x=250,y=55,width=180,height=300)
    lf_pants3=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants3.place(x=470,y=55,width=180,height=300)
    lf_pants4=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants4.place(x=690,y=55,width=180,height=300)
    lf_pants5=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants5.place(x=910,y=55,width=180,height=300)
    lf_pants6=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants6.place(x=20,y=380,width=180,height=300)
    lf_pants7=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants7.place(x=250,y=380,width=180,height=300)
    lf_pants8=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants8.place(x=470,y=380,width=180,height=300)
    lf_pants9=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants9.place(x=690,y=380,width=180,height=300)
    lf_pants10=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_pants10.place(x=910,y=380,width=180,height=300)
    label_pants_1=Label(lf_pants1,image=pants1_image,bd=2).grid(row=0,column=0)
    label_pants_2=Label(lf_pants2,image=pants2_image,bd=2).grid(row=0,column=0)
    label_pants_3=Label(lf_pants3,image=pants3_image,bd=2).grid(row=0,column=0,padx=13)
    label_pants_4=Label(lf_pants4,image=pants4_image,bd=2).grid(row=0,column=0)
    label_pants_5=Label(lf_pants5,image=pants5_image,bd=2).grid(row=0,column=0)
    label_pants_6=Label(lf_pants6,image=pants6_image,bd=2).grid(row=0,column=0)
    label_pants_7=Label(lf_pants7,image=pants7_image,bd=2).grid(row=0,column=0)
    label_pants_8=Label(lf_pants8,image=pants8_image,bd=2).grid(row=0,column=0)
    label_pants_9=Label(lf_pants9,image=pants9_image,bd=2).grid(row=0,column=0)
    label_pants_10=Label(lf_pants10,image=pants10_image,bd=2).grid(row=0,column=0)

    
    name_pants1=Label(lf_pants1,text="Washed Blue Jeans",font="arial 9").grid(row=1,column=0)
    name_pants2=Label(lf_pants2,text="Skinny Blue Jeans",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_pants3=Label(lf_pants3,text="Baggy Blue Jeans",font="arial 9",justify="center").grid(row=1,column=0)
    name_pants4=Label(lf_pants4,text="Baggy Carpenter Black Jeans",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_pants5=Label(lf_pants5,text="Baggy Lightblue jeans",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_pants6=Label(lf_pants6,text="Brown Chinos Pant",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_pants7=Label(lf_pants7,text="BLack Washed Jeans",font="arial 9",justify="center").grid(row=1,column=0)
    name_pants8=Label(lf_pants8,text="Blue Skinny Chinos Pants",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_pants9=Label(lf_pants9,text="Khakis jeans",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_pants10=Label(lf_pants10,text="Blue Plus size Jeans",font="arial 9",justify="center").grid(row=1,column=0)
    
    
    options_pants=["S","M","L","XL","XXL"]
   
    global clicked_pants1,clicked_pants2,clicked_pants3,clicked_pants4,clicked_pants5,pants_list
    global clicked_pants6,clicked_pants7,clicked_pants8,clicked_pants9,clicked_pants10
    drop_pants1=OptionMenu(lf_pants1,clicked_pants1,*options_pants).place(x=0,y=212)
    drop_pants2=OptionMenu(lf_pants2,clicked_pants2,*options_pants).place(x=0,y=212)
    drop_pants3=OptionMenu(lf_pants3,clicked_pants3,*options_pants).place(x=0,y=212)
    drop_pants4=OptionMenu(lf_pants4,clicked_pants4,*options_pants).place(x=0,y=212)
    drop_pants5=OptionMenu(lf_pants5,clicked_pants5,*options_pants).place(x=0,y=212)
    drop_pants6=OptionMenu(lf_pants6,clicked_pants6,*options_pants).place(x=0,y=212)
    drop_pants7=OptionMenu(lf_pants7,clicked_pants7,*options_pants).place(x=0,y=212)
    drop_pants8=OptionMenu(lf_pants8,clicked_pants8,*options_pants).place(x=0,y=212)
    drop_pants9=OptionMenu(lf_pants9,clicked_pants9,*options_pants).place(x=0,y=212)
    drop_pants10=OptionMenu(lf_pants10,clicked_pants10,*options_pants).place(x=0,y=212)

    def increase_quantity_pants(label):
            current_value = int(label["text"])
            label["text"] = str(current_value + 1)

    def decrease_quantity_pants(label):
        current_value = int(label["text"])
        if current_value > 1:
            label["text"] = str(current_value - 1)


    quantity_label_pants1 = Label(lf_pants1, text="1", font=("Helvetica", 16))
    quantity_label_pants1.place(x=95,y=212)
    quantity_label_pants2 = Label(lf_pants2, text="1", font=("Helvetica", 16))
    quantity_label_pants2.place(x=95,y=212)
    quantity_label_pants3 = Label(lf_pants3, text="1", font=("Helvetica", 16))
    quantity_label_pants3.place(x=95,y=212)
    quantity_label_pants4 = Label(lf_pants4, text="1", font=("Helvetica", 16))
    quantity_label_pants4.place(x=95,y=212)
    quantity_label_pants5 = Label(lf_pants5, text="1", font=("Helvetica", 16))
    quantity_label_pants5.place(x=95,y=212)
    quantity_label_pants6 = Label(lf_pants6, text="1", font=("Helvetica", 16))
    quantity_label_pants6.place(x=95,y=212)
    quantity_label_pants7 = Label(lf_pants7, text="1", font=("Helvetica", 16))
    quantity_label_pants7.place(x=95,y=212)
    quantity_label_pants8 = Label(lf_pants8, text="1", font=("Helvetica", 16))
    quantity_label_pants8.place(x=95,y=212)
    quantity_label_pants9 = Label(lf_pants9, text="1", font=("Helvetica", 16))
    quantity_label_pants9.place(x=95,y=212)
    quantity_label_pants10 = Label(lf_pants10, text="1", font=("Helvetica", 16))
    quantity_label_pants10.place(x=95,y=212)
    
    

    increase_button_pants1 = Button(lf_pants1, text="+", command=lambda:increase_quantity_pants(quantity_label_pants1), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants2 = Button(lf_pants2, text="+", command=lambda:increase_quantity_pants(quantity_label_pants2), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants3 = Button(lf_pants3, text="+", command=lambda:increase_quantity_pants(quantity_label_pants3), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants4 = Button(lf_pants4, text="+", command=lambda:increase_quantity_pants(quantity_label_pants4), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants5 = Button(lf_pants5, text="+", command=lambda:increase_quantity_pants(quantity_label_pants5), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants6 = Button(lf_pants6, text="+", command=lambda:increase_quantity_pants(quantity_label_pants6), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants7 = Button(lf_pants7, text="+", command=lambda:increase_quantity_pants(quantity_label_pants7), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants8 = Button(lf_pants8, text="+", command=lambda:increase_quantity_pants(quantity_label_pants8), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants9 = Button(lf_pants9, text="+", command=lambda:increase_quantity_pants(quantity_label_pants9), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_pants10 = Button(lf_pants10, text="+", command=lambda:increase_quantity_pants(quantity_label_pants10), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)


    decrease_button_pants1 = Button(lf_pants1, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants1), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants2 = Button(lf_pants2, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants2), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants3 = Button(lf_pants3, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants3), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants4 = Button(lf_pants4, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants4), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants5 = Button(lf_pants5, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants5), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants6 = Button(lf_pants6, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants6), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants7 = Button(lf_pants7, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants7), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants8 = Button(lf_pants8, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants8), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants9 = Button(lf_pants9, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants9), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_pants10 = Button(lf_pants10, text="-", command=lambda:decrease_quantity_pants(quantity_label_pants10), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  



    def AddG1():
        global pants_list
        quantity = int(quantity_label_pants1["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Washed Blue Jeans"
            price_per_item = 1599
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    def AddG2():
        global pants_list
        quantity = int(quantity_label_pants2["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Skinny Blue Jeans"
            price_per_item = 1699
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG3():
        global pants_list
        quantity = int(quantity_label_pants3["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Baggy Blue Jeans"
            price_per_item = 1999
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG4():
        global pants_list
        quantity = int(quantity_label_pants4["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Baggy Carpenter Black Jeans"
            price_per_item = 2199
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG5():
        global pants_list
        quantity = int(quantity_label_pants5["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Baggy Lightblue Jeans"
            price_per_item = 1699
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG6():
        global pants_list
        quantity = int(quantity_label_pants6["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Brown Chinos Pants"
            price_per_item = 1999
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG7():
        global pants_list
        quantity = int(quantity_label_pants7["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Black Washed Jeans"
            price_per_item = 2099
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG8():
        global pants_list
        quantity = int(quantity_label_pants8["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Blue Skinny Chinos Pants"
            price_per_item = 1599
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG9():
        global pants_list
        quantity = int(quantity_label_pants9["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Khakis Jeans"
            price_per_item = 2999
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddG10():
        global pants_list
        quantity = int(quantity_label_pants10["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Blue Plus Size Jeans"
            price_per_item = 1899
            total_price = quantity * price_per_item

            pants_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
   
    price_pants1=Label(lf_pants1,text="Price: Rs.1599",font="arial 9 bold").place(x=5,y=245)
    price_pants2=Label(lf_pants2,text="Price: Rs.1699",font="arial 9 bold").place(x=5,y=245)
    price_pants3=Label(lf_pants3,text="Price: Rs.1999",font="arial 9 bold").place(x=5,y=245)
    price_pants4=Label(lf_pants4,text="Price: Rs.2199",font="arial 9 bold").place(x=5,y=245)
    price_pants5=Label(lf_pants5,text="Price: Rs.1699",font="arial 9 bold").place(x=5,y=245)
    price_pants6=Label(lf_pants6,text="Price: Rs.1999",font="arial 9 bold").place(x=5,y=245)
    price_pants7=Label(lf_pants7,text="Price: Rs.2099",font="arial 9 bold").place(x=5,y=245)
    price_pants8=Label(lf_pants8,text="Price: Rs.1599",font="arial 9 bold").place(x=5,y=245)
    price_pants9=Label(lf_pants9,text="Price: Rs.2999",font="arial 9 bold").place(x=5,y=245)
    price_pants10=Label(lf_pants10,text="Price: Rs.1899",font="arial 9 bold").place(x=5,y=245)
    
    add_pants1=Button(lf_pants1,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG1,justify="right").place(x=95,y=240)
    add_pants2=Button(lf_pants2,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG2,justify="right").place(x=95,y=240)
    add_pants3=Button(lf_pants3,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG3,justify="right").place(x=95,y=240)
    add_pants4=Button(lf_pants4,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG4,justify="right").place(x=95,y=240)
    add_pants5=Button(lf_pants5,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG5,justify="right").place(x=95,y=240)
    add_pants6=Button(lf_pants6,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG6,justify="right").place(x=95,y=240)
    add_pants7=Button(lf_pants7,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG7,justify="right").place(x=95,y=240)
    add_pants8=Button(lf_pants8,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG8,justify="right").place(x=95,y=240)
    add_pants9=Button(lf_pants9,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG9,justify="right").place(x=95,y=240)
    add_pants10=Button(lf_pants10,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddG10,justify="right").place(x=95,y=240)

def TshirtCall():
    HideAllFrames()
    Tshirt_Label=Label(Products_frame,text="Tshirt",font="times 18 bold",fg="Red").grid(row=0,column=0,padx=10)
    lf_Tshirt1=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt1.place(x=20,y=55,width=200,height=300)
    lf_Tshirt2=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt2.place(x=250,y=55,width=200,height=300)
    lf_Tshirt3=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt3.place(x=470,y=55,width=200,height=300)
    lf_Tshirt4=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt4.place(x=690,y=55,width=200,height=300)
    lf_Tshirt5=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt5.place(x=910,y=55,width=200,height=300)
    lf_Tshirt6=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt6.place(x=20,y=380,width=200,height=300)
    lf_Tshirt7=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt7.place(x=250,y=380,width=200,height=300)
    lf_Tshirt8=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt8.place(x=470,y=380,width=200,height=300)
    lf_Tshirt9=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt9.place(x=690,y=380,width=200,height=300)
    lf_Tshirt10=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Tshirt10.place(x=910,y=380,width=200,height=300)
    label_Tshirt_1=Label(lf_Tshirt1,image=Tshirt1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_2=Label(lf_Tshirt2,image=Tshirt2_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_3=Label(lf_Tshirt3,image=Tshirt3_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_4=Label(lf_Tshirt4,image=Tshirt4_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_5=Label(lf_Tshirt5,image=Tshirt5_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_6=Label(lf_Tshirt6,image=Tshirt6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_7=Label(lf_Tshirt7,image=Tshirt7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Tshirt_8=Label(lf_Tshirt8,image=Tshirt8_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Tshirt_9=Label(lf_Tshirt9,image=Tshirt9_image,bd=2,justify="center").grid(row=0,column=0)
    label_Tshirt_10=Label(lf_Tshirt10,image=Tshirt10_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    
    name_Tshirt1=Label(lf_Tshirt1,text="Black Plain Tshirt",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_Tshirt2=Label(lf_Tshirt2,text="White Printed Tshirt ",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_Tshirt3=Label(lf_Tshirt3,text="Plain White Tshirt ",font="arial 9",justify="center").grid(row=1,column=0)
    name_Tshirt4=Label(lf_Tshirt4,text="Naruto Printed Off White Tshirt",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_Tshirt5=Label(lf_Tshirt5,text="Off white Plain Tshirt",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_Tshirt6=Label(lf_Tshirt6,text="Stripped Beige Tshirt",font="arial 9",justify="center").grid(row=1,column=0)
    name_Tshirt7=Label(lf_Tshirt7,text="Blue Full Polo Tshirt",font="arial 9",justify="center").grid(row=2,column=0)
    name_Tshirt8=Label(lf_Tshirt8,text="Green Round Necked Plain Tshirt",font="arial 9",justify="center").grid(row=3,column=0,padx=6)
    name_Tshirt9=Label(lf_Tshirt9,text="King Printed White Tshirt",font="arial 9",justify="center").grid(row=1,column=0)
    name_Tshirt10=Label(lf_Tshirt10,text="Plain Blue Round Neck Tshirt",font="arial 9",justify="center").grid(row=2,column=0)
    
    def increase_quantity_Tshirt(label):
            current_value = int(label["text"])
            label["text"] = str(current_value + 1)

    def decrease_quantity_Tshirt(label):
        current_value = int(label["text"])
        if current_value > 1:
            label["text"] = str(current_value - 1)


    quantity_label_Tshirt1 = Label(lf_Tshirt1, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt1.place(x=95,y=212)
    quantity_label_Tshirt2 = Label(lf_Tshirt2, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt2.place(x=95,y=212)
    quantity_label_Tshirt3 = Label(lf_Tshirt3, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt3.place(x=95,y=212)
    quantity_label_Tshirt4 = Label(lf_Tshirt4, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt4.place(x=95,y=212)
    quantity_label_Tshirt5 = Label(lf_Tshirt5, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt5.place(x=95,y=212)
    quantity_label_Tshirt6 = Label(lf_Tshirt6, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt6.place(x=95,y=212)
    quantity_label_Tshirt7 = Label(lf_Tshirt7, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt7.place(x=95,y=212)
    quantity_label_Tshirt8 = Label(lf_Tshirt8, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt8.place(x=95,y=212)
    quantity_label_Tshirt9 = Label(lf_Tshirt9, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt9.place(x=95,y=212)
    quantity_label_Tshirt10 = Label(lf_Tshirt10, text="1", font=("Helvetica", 16))
    quantity_label_Tshirt10.place(x=95,y=212)
    
    

    increase_button_Tshirt1 = Button(lf_Tshirt1, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt1), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt2 = Button(lf_Tshirt2, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt2), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt3 = Button(lf_Tshirt3, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt3), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt4 = Button(lf_Tshirt4, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt4), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt5 = Button(lf_Tshirt5, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt5), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt6 = Button(lf_Tshirt6, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt6), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt7 = Button(lf_Tshirt7, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt7), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt8 = Button(lf_Tshirt8, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt8), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt9 = Button(lf_Tshirt9, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt9), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Tshirt10 = Button(lf_Tshirt10, text="+", command=lambda:increase_quantity_Tshirt(quantity_label_Tshirt10), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)


    decrease_button_Tshirt1 = Button(lf_Tshirt1, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt1), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt2 = Button(lf_Tshirt2, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt2), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt3 = Button(lf_Tshirt3, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt3), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt4 = Button(lf_Tshirt4, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt4), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt5 = Button(lf_Tshirt5, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt5), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt6 = Button(lf_Tshirt6, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt6), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt7 = Button(lf_Tshirt7, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt7), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt8 = Button(lf_Tshirt8, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt8), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt9 = Button(lf_Tshirt9, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt9), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Tshirt10 = Button(lf_Tshirt10, text="-", command=lambda:decrease_quantity_Tshirt(quantity_label_Tshirt10), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  

    options_Tshirt=["S","M","L","XL","XXL"]
   
    global clicked_Tshirt1,clicked_Tshirt2,clicked_Tshirt3,clicked_Tshirt4,clicked_Tshirt5
    global Tshirt_list
    global clicked_Tshirt6,clicked_Tshirt7,clicked_Tshirt8,clicked_Tshirt9,clicked_Tshirt10
    drop_Tshirt1=OptionMenu(lf_Tshirt1,clicked_Tshirt1,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt2=OptionMenu(lf_Tshirt2,clicked_Tshirt2,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt3=OptionMenu(lf_Tshirt3,clicked_Tshirt3,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt4=OptionMenu(lf_Tshirt4,clicked_Tshirt4,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt5=OptionMenu(lf_Tshirt5,clicked_Tshirt5,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt6=OptionMenu(lf_Tshirt6,clicked_Tshirt6,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt7=OptionMenu(lf_Tshirt7,clicked_Tshirt7,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt8=OptionMenu(lf_Tshirt8,clicked_Tshirt8,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt9=OptionMenu(lf_Tshirt9,clicked_Tshirt9,*options_Tshirt).place(x=0,y=212)
    drop_Tshirt10=OptionMenu(lf_Tshirt10,clicked_Tshirt10,*options_Tshirt).place(x=0,y=212)
   
    def AddE1():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt1["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Black Plain Tshirt"
            price_per_item = 850
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")

    def AddE2():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt2["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "White Printed Tshirt"
            price_per_item = 999
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE3():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt3["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Plain White Tshirt"
            price_per_item = 799
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE4():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt4["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Naruto Printed Off White Tshirt"
            price_per_item = 799
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE5():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt5["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Off white Palin Tshirt"
            price_per_item = 699
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE6():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt6["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Stripped Beige Tshirt"
            price_per_item = 900
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE7():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt7["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Blue Full polo Tshirt"
            price_per_item = 1199
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE8():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt8["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Green Round Necked Tshirt"
            price_per_item = 1099
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE9():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt9["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "King Printed White Tshirt"
            price_per_item = 1299
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddE10():
        global Tshirt_list
        quantity = int(quantity_label_Tshirt10["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Plain Blue Round Neck Tshirt"
            price_per_item = 599
            total_price = quantity * price_per_item

            Tshirt_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
   
    price_Tshirt1=Label(lf_Tshirt1,text="Price: Rs.850",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt2=Label(lf_Tshirt2,text="Price: Rs.999",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt3=Label(lf_Tshirt3,text="Price: Rs.799",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt4=Label(lf_Tshirt4,text="Price: Rs.799",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt5=Label(lf_Tshirt5,text="Price: Rs.699",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt6=Label(lf_Tshirt6,text="Price: Rs.900",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt7=Label(lf_Tshirt7,text="Price: Rs.1199",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt8=Label(lf_Tshirt8,text="Price: Rs.1099",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt9=Label(lf_Tshirt9,text="Price: Rs.1299",font="arial 9 bold").place(x=5,y=245)
    price_Tshirt10=Label(lf_Tshirt10,text="Price: Rs.599",font="arial 9 bold").place(x=5,y=245)

    add_Tshirt1=Button(lf_Tshirt1,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE1,justify="right").place(x=95,y=240)
    add_Tshirt2=Button(lf_Tshirt2,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE2,justify="right").place(x=95,y=240)
    add_Tshirt3=Button(lf_Tshirt3,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE3,justify="right").place(x=95,y=240)
    add_Tshirt4=Button(lf_Tshirt4,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE4,justify="right").place(x=95,y=240)
    add_Tshirt5=Button(lf_Tshirt5,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE5,justify="right").place(x=95,y=240)
    add_Tshirt6=Button(lf_Tshirt6,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE6,justify="right").place(x=95,y=240)
    add_Tshirt7=Button(lf_Tshirt7,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE7,justify="right").place(x=95,y=240)
    add_Tshirt8=Button(lf_Tshirt8,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE8,justify="right").place(x=95,y=240)
    add_Tshirt9=Button(lf_Tshirt9,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE9,justify="right").place(x=95,y=240)
    add_Tshirt10=Button(lf_Tshirt10,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddE10,justify="right").place(x=95,y=240)
def shoesCall():
    HideAllFrames()
    Shoes_Label=Label(Products_frame,text="Shoes",font="times 18 bold",fg="Red").grid(row=0,column=0,padx=10)
    lf_shoes1=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes1.place(x=20,y=55,width=200,height=300)
    lf_shoes2=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes2.place(x=250,y=55,width=200,height=300)
    lf_shoes3=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes3.place(x=470,y=55,width=200,height=300)
    lf_shoes4=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes4.place(x=690,y=55,width=200,height=300)
    lf_shoes5=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes5.place(x=910,y=55,width=200,height=300)
    lf_shoes6=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes6.place(x=20,y=380,width=200,height=300)
    lf_shoes7=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes7.place(x=250,y=380,width=200,height=300)
    lf_shoes8=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes8.place(x=470,y=380,width=200,height=300)
    lf_shoes9=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes9.place(x=690,y=380,width=200,height=300)
    lf_shoes10=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_shoes10.place(x=910,y=380,width=200,height=300)
    label_shoes_1=Label(lf_shoes1,image=shoes1_image,bd=2,justify="center").grid(row=0,column=0)
    label_shoes_2=Label(lf_shoes2,image=shoes2_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_shoes_3=Label(lf_shoes3,image=shoes3_image,bd=2,justify="center").grid(row=0,column=0)
    label_shoes_4=Label(lf_shoes4,image=shoes4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_shoes_5=Label(lf_shoes5,image=shoes5_image,bd=2,justify="center").grid(row=0,column=0)
    label_shoes_6=Label(lf_shoes6,image=shoes6_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_shoes_7=Label(lf_shoes7,image=shoes7_image,bd=2,justify="center").grid(row=0,column=0)
    label_shoes_8=Label(lf_shoes8,image=shoes8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_shoes_9=Label(lf_shoes9,image=shoes9_image,bd=2,justify="center").grid(row=0,column=0)
    label_shoes_10=Label(lf_shoes10,image=shoes10_image,bd=2,justify="center").grid(row=0,column=0)
    
    name_shoes1=Label(lf_shoes1,text="Air Jordan-1-Element",font="arial 9",justify="center").grid(row=1,column=0,padx=13)
    name_shoes2=Label(lf_shoes2,text="Air Jordan 1 Retro",font="arial 9",justify="center").grid(row=1,column=0)
    name_shoes3=Label(lf_shoes3,text="Air Max ishodmens",font="arial 9",justify="center").grid(row=1,column=0)
    name_shoes4=Label(lf_shoes4,text="Air Vapormax Plus",font="arial 9",justify="center").grid(row=1,column=0)
    name_shoes5=Label(lf_shoes5,text="Air Max 90 goretex",font="arial 9",justify="center").grid(row=1,column=0,padx=14)
    name_shoes6=Label(lf_shoes6,text="Nike Sb dunk Low retro",font="arial 9",justify="center").grid(row=1,column=0)
    name_shoes7=Label(lf_shoes7,text="Nike Sb dunk low Panda",font="arial 9",justify="center").grid(row=2,column=0)
    name_shoes8=Label(lf_shoes8,text="Air Jordan High TopG",font="arial 9",justify="center").grid(row=1,column=0,padx=4)
    name_shoes9=Label(lf_shoes9,text="Nike Blazer Phantom mid",font="arial 9",justify="center").grid(row=2,column=0)
    name_shoes10=Label(lf_shoes10,text="Air jordan xxxviii low fun",font="arial 9",justify="center").grid(row=3,column=0)

   

    def increase_quantity_shoes(label):
            current_value = int(label["text"])
            label["text"] = str(current_value + 1)

    def decrease_quantity_shoes(label):
        current_value = int(label["text"])
        if current_value > 1:
            label["text"] = str(current_value - 1)


    quantity_label_shoes1 = Label(lf_shoes1, text="1", font=("Helvetica", 16))
    quantity_label_shoes1.place(x=95,y=212)
    quantity_label_shoes2 = Label(lf_shoes2, text="1", font=("Helvetica", 16))
    quantity_label_shoes2.place(x=95,y=212)
    quantity_label_shoes3 = Label(lf_shoes3, text="1", font=("Helvetica", 16))
    quantity_label_shoes3.place(x=95,y=212)
    quantity_label_shoes4 = Label(lf_shoes4, text="1", font=("Helvetica", 16))
    quantity_label_shoes4.place(x=95,y=212)
    quantity_label_shoes5 = Label(lf_shoes5, text="1", font=("Helvetica", 16))
    quantity_label_shoes5.place(x=95,y=212)
    quantity_label_shoes6 = Label(lf_shoes6, text="1", font=("Helvetica", 16))
    quantity_label_shoes6.place(x=95,y=212)
    quantity_label_shoes7 = Label(lf_shoes7, text="1", font=("Helvetica", 16))
    quantity_label_shoes7.place(x=95,y=212)
    quantity_label_shoes8 = Label(lf_shoes8, text="1", font=("Helvetica", 16))
    quantity_label_shoes8.place(x=95,y=212)
    quantity_label_shoes9 = Label(lf_shoes9, text="1", font=("Helvetica", 16))
    quantity_label_shoes9.place(x=95,y=212)
    quantity_label_shoes10 = Label(lf_shoes10, text="1", font=("Helvetica", 16))
    quantity_label_shoes10.place(x=95,y=212)
    
    

    increase_button_shoes1 = Button(lf_shoes1, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes1), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes2 = Button(lf_shoes2, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes2), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes3 = Button(lf_shoes3, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes3), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes4 = Button(lf_shoes4, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes4), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes5 = Button(lf_shoes5, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes5), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes6 = Button(lf_shoes6, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes6), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes7 = Button(lf_shoes7, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes7), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes8 = Button(lf_shoes8, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes8), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes9 = Button(lf_shoes9, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes9), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_shoes10 = Button(lf_shoes10, text="+", command=lambda:increase_quantity_shoes(quantity_label_shoes10), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)


    decrease_button_shoes1 = Button(lf_shoes1, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes1), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes2 = Button(lf_shoes2, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes2), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes3 = Button(lf_shoes3, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes3), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes4 = Button(lf_shoes4, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes4), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes5 = Button(lf_shoes5, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes5), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes6 = Button(lf_shoes6, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes6), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes7 = Button(lf_shoes7, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes7), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes8 = Button(lf_shoes8, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes8), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes9 = Button(lf_shoes9, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes9), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_shoes10 = Button(lf_shoes10, text="-", command=lambda:decrease_quantity_shoes(quantity_label_shoes10), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  



    


    
    options_shoes=["7","7.5","8","8.5","9","9.5","10"]

    global clicked_shoes1,clicked_shoes2,clicked_shoes3,clicked_shoes4,clicked_shoes5
    global shoes_list
    global clicked_shoes6,clicked_shoes7,clicked_shoes8,clicked_shoes9,clicked_shoes10
    drop_shoes1=OptionMenu(lf_shoes1,clicked_shoes1,*options_shoes).place(x=0,y=212)
    drop_shoes2=OptionMenu(lf_shoes2,clicked_shoes2,*options_shoes).place(x=0,y=212)
    drop_shoes3=OptionMenu(lf_shoes3,clicked_shoes3,*options_shoes).place(x=0,y=212)
    drop_shoes4=OptionMenu(lf_shoes4,clicked_shoes4,*options_shoes).place(x=0,y=212)
    drop_shoes5=OptionMenu(lf_shoes5,clicked_shoes5,*options_shoes).place(x=0,y=212)
    drop_shoes6=OptionMenu(lf_shoes6,clicked_shoes6,*options_shoes).place(x=0,y=212)
    drop_shoes7=OptionMenu(lf_shoes7,clicked_shoes7,*options_shoes).place(x=0,y=212)
    drop_shoes8=OptionMenu(lf_shoes8,clicked_shoes8,*options_shoes).place(x=0,y=212)
    drop_shoes9=OptionMenu(lf_shoes9,clicked_shoes9,*options_shoes).place(x=0,y=212)
    drop_shoes10=OptionMenu(lf_shoes10,clicked_shoes10,*options_shoes).place(x=0,y=212)
    
    price_shoes1=Label(lf_shoes1,text="Price: Rs.10,000",font="arial 9 bold").place(x=5,y=245)
    price_shoes2=Label(lf_shoes2,text="Price: Rs.15,000",font="arial 9 bold").place(x=5,y=245)
    price_shoes3=Label(lf_shoes3,text="Price: Rs.15,500",font="arial 9 bold").place(x=5,y=245)
    price_shoes4=Label(lf_shoes4,text="Price: Rs.23,500",font="arial 9 bold").place(x=5,y=245)
    price_shoes5=Label(lf_shoes5,text="Price: Rs.19,800",font="arial 9 bold").place(x=5,y=245)
    price_shoes6=Label(lf_shoes6,text="Price: Rs.28,990",font="arial 9 bold").place(x=5,y=245)
    price_shoes7=Label(lf_shoes7,text="Price: Rs.9,000",font="arial 9 bold").place(x=5,y=245)
    price_shoes8=Label(lf_shoes8,text="Price: Rs.6,799",font="arial 9 bold").place(x=5,y=245)
    price_shoes9=Label(lf_shoes9,text="Price: Rs.16,999",font="arial 9 bold").place(x=5,y=245)
    price_shoes10=Label(lf_shoes10,text="Price: Rs.12,999",font="arial 9 bold").place(x=5,y=245)
    def AddS1():
        global shoes_list
        quantity = int(quantity_label_shoes1["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Jordan -1 Element"
            price_per_item = 10000
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")

    def AddS2():
        global shoes_list
        quantity = int(quantity_label_shoes2["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Jordan 1 Retro"
            price_per_item = 15000
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS3():
        global shoes_list
        quantity = int(quantity_label_shoes3["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Max Ishodemns"
            price_per_item = 15500
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS4():
        global shoes_list
        quantity = int(quantity_label_shoes4["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Vapormax Plus"
            price_per_item = 23500
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS5():
        global shoes_list
        quantity = int(quantity_label_shoes5["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Max 90 Goretex"
            price_per_item = 19800
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS6():
        global shoes_list
        quantity = int(quantity_label_shoes6["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Nike SB dunk low retro"
            price_per_item = 28990
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS7():
        global shoes_list
        quantity = int(quantity_label_shoes7["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Nike Sb dunk low panda"
            price_per_item = 9000
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS8():
        global shoes_list
        quantity = int(quantity_label_shoes8["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Jordan High TopG"
            price_per_item = 6799
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS9():
        global shoes_list
        quantity = int(quantity_label_shoes9["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Nike Blazer Phantom Mid"
            price_per_item = 16999
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddS10():
        global shoes_list
        quantity = int(quantity_label_shoes10["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Air Jordan xxxviii Low fun"
            price_per_item = 12999
            total_price = quantity * price_per_item

            shoes_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
   
    add_shoes1=Button(lf_shoes1,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS1).place(x=98,y=245)
    add_shoes2=Button(lf_shoes2,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS2).place(x=98,y=245)
    add_shoes3=Button(lf_shoes3,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS3).place(x=98,y=245)
    add_shoes4=Button(lf_shoes4,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS4).place(x=98,y=245)
    add_shoes5=Button(lf_shoes5,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS5).place(x=98,y=245)
    add_shoes6=Button(lf_shoes6,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS6).place(x=98,y=245)
    add_shoes7=Button(lf_shoes7,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS7).place(x=98,y=245)
    add_shoes8=Button(lf_shoes8,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS8).place(x=98,y=245)
    add_shoes9=Button(lf_shoes9,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS9).place(x=98,y=245)
    add_shoes10=Button(lf_shoes10,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddS10).place(x=98,y=245)

def HoodieCall():
    HideAllFrames()
    Hoodie_Label=Label(Products_frame,text="Hoodie",font="times 18 bold",fg="Red").grid(row=0,column=0,padx=20)
    lf_Hoodie1=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie1.place(x=20,y=55,width=200,height=300)
    lf_Hoodie2=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie2.place(x=250,y=55,width=200,height=300)
    lf_Hoodie3=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie3.place(x=470,y=55,width=200,height=300)
    lf_Hoodie4=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie4.place(x=690,y=55,width=200,height=300)
    lf_Hoodie5=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie5.place(x=910,y=55,width=200,height=300)
    lf_Hoodie6=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie6.place(x=20,y=380,width=200,height=300)
    lf_Hoodie7=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie7.place(x=250,y=380,width=200,height=300)
    lf_Hoodie8=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie8.place(x=470,y=380,width=200,height=300)
    lf_Hoodie9=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie9.place(x=690,y=380,width=200,height=300)
    lf_Hoodie10=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Hoodie10.place(x=910,y=380,width=200,height=300)
    label_Hoodie_1=Label(lf_Hoodie1,image=Hoodie1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Hoodie_2=Label(lf_Hoodie2,image=Hoodie2_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Hoodie_3=Label(lf_Hoodie3,image=Hoodie3_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Hoodie_4=Label(lf_Hoodie4,image=Hoodie4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Hoodie_5=Label(lf_Hoodie5,image=Hoodie5_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Hoodie_6=Label(lf_Hoodie6,image=Hoodie6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Hoodie_7=Label(lf_Hoodie7,image=Hoodie7_image,bd=2,justify="center").grid(row=0,column=0)
    label_Hoodie_8=Label(lf_Hoodie8,image=Hoodie8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Hoodie_9=Label(lf_Hoodie9,image=Hoodie9_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Hoodie_10=Label(lf_Hoodie10,image=Hoodie10_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    
    name_Hoodie1=Label(lf_Hoodie1,text="White Plain Fleece Hoodie",font="arial 9",justify="center").grid(row=1,column=0,padx=10)
    name_Hoodie2=Label(lf_Hoodie2,text="Off white Fleece Hoodie",font="arial 9",justify="center").grid(row=1,column=0)
    name_Hoodie3=Label(lf_Hoodie3,text="Essentials Off white Hoodie",font="arial 9",justify="center").grid(row=2,column=0)
    name_Hoodie4=Label(lf_Hoodie4,text="Dual color printed Hoodie",font="arial 9",justify="center").grid(row=1,column=0)
    name_Hoodie5=Label(lf_Hoodie5,text="Human Embroided Brown Hoodie",font="arial 9",justify="center").grid(row=2,column=0)
    name_Hoodie6=Label(lf_Hoodie6,text="Red & Black Fire hoodie",font="arial 9",justify="center").grid(row=1,column=0)
    name_Hoodie7=Label(lf_Hoodie7,text="Plain Blue Hoodie",font="arial 9",justify="center").grid(row=2,column=0)
    name_Hoodie8=Label(lf_Hoodie8,text="Spiderman Black Hoodie Limited Edition",font="arial 9",justify="center").grid(row=3,column=0)
    name_Hoodie9=Label(lf_Hoodie9,text="Female Rose hoodie",font="arial 9",justify="center").grid(row=1,column=0)
    name_Hoodie10=Label(lf_Hoodie10,text="Couple Hoodie Winter Edition",font="arial 9",justify="center").grid(row=2,column=0)
    
    

    def increase_quantity_Hoodie(label):
            current_value = int(label["text"])
            label["text"] = str(current_value + 1)

    def decrease_quantity_Hoodie(label):
        current_value = int(label["text"])
        if current_value > 1:
            label["text"] = str(current_value - 1)


    quantity_label_Hoodie1 = Label(lf_Hoodie1, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie1.place(x=95,y=212)
    quantity_label_Hoodie2 = Label(lf_Hoodie2, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie2.place(x=95,y=212)
    quantity_label_Hoodie3 = Label(lf_Hoodie3, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie3.place(x=95,y=212)
    quantity_label_Hoodie4 = Label(lf_Hoodie4, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie4.place(x=95,y=212)
    quantity_label_Hoodie5 = Label(lf_Hoodie5, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie5.place(x=95,y=212)
    quantity_label_Hoodie6 = Label(lf_Hoodie6, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie6.place(x=95,y=212)
    quantity_label_Hoodie7 = Label(lf_Hoodie7, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie7.place(x=95,y=212)
    quantity_label_Hoodie8 = Label(lf_Hoodie8, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie8.place(x=95,y=212)
    quantity_label_Hoodie9 = Label(lf_Hoodie9, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie9.place(x=95,y=212)
    quantity_label_Hoodie10 = Label(lf_Hoodie10, text="1", font=("Helvetica", 16))
    quantity_label_Hoodie10.place(x=95,y=212)
    
    

    increase_button_Hoodie1 = Button(lf_Hoodie1, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie1), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie2 = Button(lf_Hoodie2, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie2), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie3 = Button(lf_Hoodie3, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie3), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie4 = Button(lf_Hoodie4, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie4), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie5 = Button(lf_Hoodie5, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie5), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie6 = Button(lf_Hoodie6, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie6), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie7 = Button(lf_Hoodie7, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie7), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie8 = Button(lf_Hoodie8, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie8), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie9 = Button(lf_Hoodie9, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie9), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Hoodie10 = Button(lf_Hoodie10, text="+", command=lambda:increase_quantity_Hoodie(quantity_label_Hoodie10), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)


    decrease_button_Hoodie1 = Button(lf_Hoodie1, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie1), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie2 = Button(lf_Hoodie2, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie2), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie3 = Button(lf_Hoodie3, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie3), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie4 = Button(lf_Hoodie4, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie4), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie5 = Button(lf_Hoodie5, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie5), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie6 = Button(lf_Hoodie6, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie6), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie7 = Button(lf_Hoodie7, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie7), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie8 = Button(lf_Hoodie8, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie8), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie9 = Button(lf_Hoodie9, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie9), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Hoodie10 = Button(lf_Hoodie10, text="-", command=lambda:decrease_quantity_Hoodie(quantity_label_Hoodie10), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  



    options_Hoodie=["S","M","L","XL","XXL"]
    global clicked_Hoodie1,clicked_Hoodie2,clicked_Hoodie3,clicked_Hoodie4,clicked_Hoodie5
    global Hoodie_list
    global clicked_Hoodie6,clicked_Hoodie7,clicked_Hoodie8,clicked_Hoodie9,clicked_Hoodie10
    drop_Hoodie1=OptionMenu(lf_Hoodie1,clicked_Hoodie1,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie2=OptionMenu(lf_Hoodie2,clicked_Hoodie2,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie3=OptionMenu(lf_Hoodie3,clicked_Hoodie3,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie4=OptionMenu(lf_Hoodie4,clicked_Hoodie4,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie5=OptionMenu(lf_Hoodie5,clicked_Hoodie5,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie6=OptionMenu(lf_Hoodie6,clicked_Hoodie6,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie7=OptionMenu(lf_Hoodie7,clicked_Hoodie7,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie8=OptionMenu(lf_Hoodie8,clicked_Hoodie8,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie9=OptionMenu(lf_Hoodie9,clicked_Hoodie9,*options_Hoodie).place(x=0,y=212)
    drop_Hoodie10=OptionMenu(lf_Hoodie10,clicked_Hoodie10,*options_Hoodie).place(x=0,y=212)
    

    price_Hoodie1=Label(lf_Hoodie1,text="Price: Rs.1850",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie2=Label(lf_Hoodie2,text="Price: Rs.1999",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie3=Label(lf_Hoodie3,text="Price: Rs.1799",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie4=Label(lf_Hoodie4,text="Price: Rs.1799",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie5=Label(lf_Hoodie5,text="Price: Rs.1699",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie6=Label(lf_Hoodie6,text="Price: Rs.1900",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie7=Label(lf_Hoodie7,text="Price: Rs.2199",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie8=Label(lf_Hoodie8,text="Price: Rs.1899",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie9=Label(lf_Hoodie9,text="Price: Rs.1599",font="arial 9 bold").place(x=5,y=245)
    price_Hoodie10=Label(lf_Hoodie10,text="Price: Rs.2599",font="arial 9 bold").place(x=5,y=245)
    
    def AddF1():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie1["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "White Plain Fleece Hoodie"
            price_per_item = 1850
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")

    
    def AddF2():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie2["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Off white Fleece Hoodie"
            price_per_item = 1999
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    def AddF3():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie3["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Essentials Off White Hoodie"
            price_per_item = 1799
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddF4():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie4["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Dual Color Printed Hoodie"
            price_per_item = 1799
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    
    def AddF5():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie5["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Human Embroided Brown Hoodie"
            price_per_item = 1699
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    def AddF6():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie6["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Red & Black Fire Hoodie"
            price_per_item = 1900
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    def AddF7():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie7["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Plain Blue Hoodie"
            price_per_item = 2199
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    def AddF8():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie8["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Spiderman Balck Hoodie Limited Edition"
            price_per_item = 1899
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    def AddF9():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie9["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Female Rose Hoodie"
            price_per_item = 1599
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    
    def AddF10():
        global Hoodie_list
        quantity = int(quantity_label_Hoodie10["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Couple Hoodie Winter Edition"
            price_per_item = 2599
            total_price = quantity * price_per_item

            Hoodie_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    
    add_Hoodie1=Button(lf_Hoodie1,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF1,justify="right").place(x=95,y=240)
    add_Hoodie2=Button(lf_Hoodie2,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF2,justify="right").place(x=95,y=240)
    add_Hoodie3=Button(lf_Hoodie3,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF3,justify="right").place(x=95,y=240)
    add_Hoodie4=Button(lf_Hoodie4,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF4,justify="right").place(x=95,y=240)
    add_Hoodie5=Button(lf_Hoodie5,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF5,justify="right").place(x=95,y=240)
    add_Hoodie6=Button(lf_Hoodie6,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF6,justify="right").place(x=95,y=240)
    add_Hoodie7=Button(lf_Hoodie7,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF7,justify="right").place(x=95,y=240)
    add_Hoodie8=Button(lf_Hoodie8,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF8,justify="right").place(x=95,y=240)
    add_Hoodie9=Button(lf_Hoodie9,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF9,justify="right").place(x=95,y=240)
    add_Hoodie10=Button(lf_Hoodie10,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddF10,justify="right").place(x=95,y=240)


def JacketCall():
    HideAllFrames()
    Jacket_Label=Label(Products_frame,text="Jacket",font="times 18 bold",fg="Red").grid(row=0,column=0,padx=20)
    lf_Jacket1=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket1.place(x=20,y=55,width=200,height=300)
    lf_Jacket2=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket2.place(x=250,y=55,width=200,height=300)
    lf_Jacket3=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket3.place(x=470,y=55,width=200,height=300)
    lf_Jacket4=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket4.place(x=690,y=55,width=200,height=300)
    lf_Jacket5=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket5.place(x=910,y=55,width=200,height=300)
    lf_Jacket6=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket6.place(x=20,y=380,width=200,height=300)
    lf_Jacket7=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket7.place(x=250,y=380,width=200,height=300)
    lf_Jacket8=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket8.place(x=470,y=380,width=200,height=300)
    lf_Jacket9=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket9.place(x=690,y=380,width=200,height=300)
    lf_Jacket10=LabelFrame(Products_frame,bd=2,relief="flat")
    lf_Jacket10.place(x=910,y=380,width=200,height=300)
    label_Jacket_1=Label(lf_Jacket1,image=Jacket1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Jacket_2=Label(lf_Jacket2,image=Jacket2_image,bd=2,justify="center").grid(row=0,column=0)
    label_Jacket_3=Label(lf_Jacket3,image=Jacket3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Jacket_4=Label(lf_Jacket4,image=Jacket4_image,bd=2,justify="center").grid(row=0,column=0)
    label_Jacket_5=Label(lf_Jacket5,image=Jacket5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Jacket_6=Label(lf_Jacket6,image=Jacket6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Jacket_7=Label(lf_Jacket7,image=Jacket7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Jacket_8=Label(lf_Jacket8,image=Jacket8_image,bd=2,justify="center").grid(row=0,column=0)
    label_Jacket_9=Label(lf_Jacket9,image=Jacket9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_Jacket_10=Label(lf_Jacket10,image=Jacket10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_Jacket1=Label(lf_Jacket1,text="Men's Winter Casual Bomber Jacket",font="arial 9",justify="center").grid(row=1,column=0)
    name_Jacket2=Label(lf_Jacket2,text="Men’s Winter Heavy Fur Jacket",font="arial 9",justify="center").grid(row=1,column=0)
    name_Jacket3=Label(lf_Jacket3,text="Inside Fur Winter Jacket for Men ",font="arial 9",justify="center").grid(row=1,column=0)
    name_Jacket4=Label(lf_Jacket4,text="NYXT 11-09 Korean Japanese For Men",font="arial 9",justify="center").grid(row=2,column=0)
    name_Jacket5=Label(lf_Jacket5,text="Silicon Hooded Jacket For Men",font="arial 9",justify="center").grid(row=1,column=0)
    name_Jacket6=Label(lf_Jacket6,text="3 Layer Full Sleeve Hooded Silicon Jacket",font="arial 9",justify="center").grid(row=1,column=0)
    name_Jacket7=Label(lf_Jacket7,text="Womens Softshell Primaloft Insulate Jacket",font="arial 9",justify="center").grid(row=2,column=0)
    name_Jacket8=Label(lf_Jacket8,text="Men’s Winter Heavy Fur Jacket",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_Jacket9=Label(lf_Jacket9,text="Winter Front Zipper Fiber Sleeveless Jacket",font="arial 9",justify="center").grid(row=1,column=0)
    name_Jacket10=Label(lf_Jacket10,text="Classic Vintage Black Winter Leather Jacket",font="arial 9",justify="center").grid(row=1,column=0)
    
    def increase_quantity_Jacket(label):
            current_value = int(label["text"])
            label["text"] = str(current_value + 1)

    def decrease_quantity_Jacket(label):
        current_value = int(label["text"])
        if current_value > 1:
            label["text"] = str(current_value - 1)


    quantity_label_Jacket1 = Label(lf_Jacket1, text="1", font=("Helvetica", 16))
    quantity_label_Jacket1.place(x=95,y=212)
    quantity_label_Jacket2 = Label(lf_Jacket2, text="1", font=("Helvetica", 16))
    quantity_label_Jacket2.place(x=95,y=212)
    quantity_label_Jacket3 = Label(lf_Jacket3, text="1", font=("Helvetica", 16))
    quantity_label_Jacket3.place(x=95,y=212)
    quantity_label_Jacket4 = Label(lf_Jacket4, text="1", font=("Helvetica", 16))
    quantity_label_Jacket4.place(x=95,y=212)
    quantity_label_Jacket5 = Label(lf_Jacket5, text="1", font=("Helvetica", 16))
    quantity_label_Jacket5.place(x=95,y=212)
    quantity_label_Jacket6 = Label(lf_Jacket6, text="1", font=("Helvetica", 16))
    quantity_label_Jacket6.place(x=95,y=212)
    quantity_label_Jacket7 = Label(lf_Jacket7, text="1", font=("Helvetica", 16))
    quantity_label_Jacket7.place(x=95,y=212)
    quantity_label_Jacket8 = Label(lf_Jacket8, text="1", font=("Helvetica", 16))
    quantity_label_Jacket8.place(x=95,y=212)
    quantity_label_Jacket9 = Label(lf_Jacket9, text="1", font=("Helvetica", 16))
    quantity_label_Jacket9.place(x=95,y=212)
    quantity_label_Jacket10 = Label(lf_Jacket10, text="1", font=("Helvetica", 16))
    quantity_label_Jacket10.place(x=95,y=212)
    
    

    increase_button_Jacket1 = Button(lf_Jacket1, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket1), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket2 = Button(lf_Jacket2, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket2), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket3 = Button(lf_Jacket3, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket3), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket4 = Button(lf_Jacket4, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket4), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket5 = Button(lf_Jacket5, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket5), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket6 = Button(lf_Jacket6, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket6), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket7 = Button(lf_Jacket7, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket7), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket8 = Button(lf_Jacket8, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket8), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket9 = Button(lf_Jacket9, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket9), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)
    increase_button_Jacket10 = Button(lf_Jacket10, text="+", command=lambda:increase_quantity_Jacket(quantity_label_Jacket10), font=("Helvetica", 12),width=20,padx=5).place(x=75, y=212)


    decrease_button_Jacket1 = Button(lf_Jacket1, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket1), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket2 = Button(lf_Jacket2, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket2), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket3 = Button(lf_Jacket3, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket3), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket4 = Button(lf_Jacket4, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket4), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket5 = Button(lf_Jacket5, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket5), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket6 = Button(lf_Jacket6, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket6), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket7 = Button(lf_Jacket7, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket7), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket8 = Button(lf_Jacket8, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket8), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket9 = Button(lf_Jacket9, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket9), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  
    decrease_button_Jacket10 = Button(lf_Jacket10, text="-", command=lambda:decrease_quantity_Jacket(quantity_label_Jacket10), font=("Helvetica", 12), width=20,padx=5).place(x=110, y=212)  

   

    options_Jacket=["S","M","L","XL","XXL"]
    global clicked_Jacket1,clicked_Jacket2,clicked_Jacket3,clicked_Jacket4,clicked_Jacket5
    global Jacket_list
    global clicked_Jacket6,clicked_Jacket7,clicked_Jacket8,clicked_Jacket9,clicked_Jacket10
    drop_Jacket1=OptionMenu(lf_Jacket1,clicked_Jacket1,*options_Jacket).place(x=0,y=212)
    drop_Jacket2=OptionMenu(lf_Jacket2,clicked_Jacket2,*options_Jacket).place(x=0,y=212)
    drop_Jacket3=OptionMenu(lf_Jacket3,clicked_Jacket3,*options_Jacket).place(x=0,y=212)
    drop_Jacket4=OptionMenu(lf_Jacket4,clicked_Jacket4,*options_Jacket).place(x=0,y=212)
    drop_Jacket5=OptionMenu(lf_Jacket5,clicked_Jacket5,*options_Jacket).place(x=0,y=212)
    drop_Jacket6=OptionMenu(lf_Jacket6,clicked_Jacket6,*options_Jacket).place(x=0,y=212)
    drop_Jacket7=OptionMenu(lf_Jacket7,clicked_Jacket7,*options_Jacket).place(x=0,y=212)
    drop_Jacket8=OptionMenu(lf_Jacket8,clicked_Jacket8,*options_Jacket).place(x=0,y=212)
    drop_Jacket9=OptionMenu(lf_Jacket9,clicked_Jacket9,*options_Jacket).place(x=0,y=212)
    drop_Jacket10=OptionMenu(lf_Jacket10,clicked_Jacket10,*options_Jacket).place(x=0,y=212)


    price_Jacket1=Label(lf_Jacket1,text="Price: Rs.2850",font="arial 9 bold").place(x=5,y=245)
    price_Jacket2=Label(lf_Jacket2,text="Price: Rs.2999",font="arial 9 bold").place(x=5,y=245)
    price_Jacket3=Label(lf_Jacket3,text="Price: Rs.2799",font="arial 9 bold").place(x=5,y=245)
    price_Jacket4=Label(lf_Jacket4,text="Price: Rs.2799",font="arial 9 bold").place(x=5,y=245)
    price_Jacket5=Label(lf_Jacket5,text="Price: Rs.2699",font="arial 9 bold").place(x=5,y=245)
    price_Jacket6=Label(lf_Jacket6,text="Price: Rs.1900",font="arial 9 bold").place(x=5,y=245)
    price_Jacket7=Label(lf_Jacket7,text="Price: Rs.2500",font="arial 9 bold").place(x=5,y=245)
    price_Jacket8=Label(lf_Jacket8,text="Price: Rs.1800",font="arial 9 bold").place(x=5,y=245)
    price_Jacket9=Label(lf_Jacket9,text="Price: Rs.2599",font="arial 9 bold").place(x=5,y=245)
    price_Jacket10=Label(lf_Jacket10,text="Price: Rs.2500",font="arial 9 bold").place(x=5,y=245)

    def AddA1():
        global Jacket_list
        quantity = int(quantity_label_Jacket1["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Men's Winter Casual Bomber Jacket"
            price_per_item = 2850
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")

    def AddA2():
        global Jacket_list
        quantity = int(quantity_label_Jacket2["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Men's winter Heavy Fur Jacket"
            price_per_item = 2999
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA3():
        global Jacket_list
        quantity = int(quantity_label_Jacket3["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Inside fur Winter Jacket for Men"
            price_per_item = 2799
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA4():
        global Jacket_list
        quantity = int(quantity_label_Jacket4["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "NYXT 11-09 Korean Japanese For Men"
            price_per_item = 2799
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA5():
        global Jacket_list
        quantity = int(quantity_label_Jacket5["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Silicon Hooded Jacket for Men"
            price_per_item = 2699
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA6():
        global Jacket_list
        quantity = int(quantity_label_Jacket6["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "3 Layer Full Sleeve Hooded Silicon Jacket"
            price_per_item = 1900
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA7():
        global Jacket_list
        quantity = int(quantity_label_Jacket7["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Women's Softshell Primaloft Insulate Jacket"
            price_per_item = 2500
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA8():
        global Jacket_list
        quantity = int(quantity_label_Jacket8["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Men's winter Heavy Fur Jacket"
            price_per_item = 1800
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA9():
        global Jacket_list
        quantity = int(quantity_label_Jacket9["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Winter Frontzipper Fiber Sleeveless Jacket"
            price_per_item = 2599
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
    def AddA10():
        global Jacket_list
        quantity = int(quantity_label_Jacket10["text"])
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            product_name = "Classic Vintage Black Winter Leather Jacket"
            price_per_item = 2500
            total_price = quantity * price_per_item

            Jacket_list.append([product_name, total_price,quantity, f"Rs.{total_price}", Spaces(40 - len(product_name))])

            messagebox.showinfo("Product Status", f"{product_name} ({quantity}) added to the cart.")
            
        else:
           messagebox.showinfo("Product Status", f"{product_name} is not added to the cart.")
   

    add_Jacket1=Button(lf_Jacket1,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA1,justify="right").place(x=95,y=240)
    add_Jacket2=Button(lf_Jacket2,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA2,justify="right").place(x=95,y=240)
    add_Jacket3=Button(lf_Jacket3,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA3,justify="right").place(x=95,y=240)
    add_Jacket4=Button(lf_Jacket4,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA4,justify="right").place(x=95,y=240)
    add_Jacket5=Button(lf_Jacket5,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA5,justify="right").place(x=95,y=240)
    add_Jacket6=Button(lf_Jacket6,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA6,justify="right").place(x=95,y=240)
    add_Jacket7=Button(lf_Jacket7,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA7,justify="right").place(x=95,y=240)
    add_Jacket8=Button(lf_Jacket8,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA8,justify="right").place(x=95,y=240)
    add_Jacket9=Button(lf_Jacket9,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA9,justify="right").place(x=95,y=240)
    add_Jacket10=Button(lf_Jacket10,text="Add Item",bg="green",fg="black",font="times 9 bold",command=AddA10,justify="right").place(x=95,y=240)
pants_button=Button(Button_frame,text="Pants",font="times 20 bold",command=pantsCall)
pants_button.grid(row=0,column=0,padx=10,pady=10)
Tshirt_button=Button(Button_frame,text="Tshirt",font="times 20 bold",command=TshirtCall)
Tshirt_button.grid(row=1,column=0,padx=10,pady=10)
shoes_button=Button(Button_frame,text="Shoes",font="times 20 bold",command=shoesCall)
shoes_button.grid(row=2,column=0,padx=10,pady=10)
Hoodie_button=Button(Button_frame,text="Hoodie",font="times 20 bold",command=HoodieCall)
Hoodie_button.grid(row=3,column=0,padx=10,pady=10)

Jacket_button=Button(Button_frame,text="Jacket",font="times 20 bold",command=JacketCall)
Jacket_button.grid(row=4,column=0,padx=10,pady=10)

def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        bill_gen_button.destroy()
        pants_price=0
        Tshirt_price=0
        shoes_price=0
        Hoodie_price=0
        Jacket_price=0
        for i in range(len(pants_list)):
            pants_price+=pants_list[i][1]
        for i in range(len(Tshirt_list)):
            Tshirt_price+=Tshirt_list[i][1]
        for i in range(len(shoes_list)):
            shoes_price+=shoes_list[i][1]
        for i in range(len(Hoodie_list)):
            Hoodie_price+=Hoodie_list[i][1]
        for i in range(len(Jacket_list)):
            Jacket_price+=Jacket_list[i][1]
        total_price=pants_price+Tshirt_price+shoes_price+Hoodie_price+Jacket_price
        bill_area=LabelFrame(root,bd=2,relief="groove")
        bill_area.place(x=350,y=90,width=750,height=600)
        bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
        scroll_y=Scrollbar(bill_area,orient=VERTICAL)
        bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=bill_txt_area.yview)
        bill_txt_area.pack(fill=BOTH,expand=1)
       
        bill_txt_area.insert(END,Spaces(40)+"Luga Pasal\n"+Spaces(90,'*')+"\n")
        
        if len(Tshirt_list)>0:
                bill_txt_area.insert(END,"Tshirt Product(s)\n\nProduct Name"+" " * 28+"Price\n")
                for i in Tshirt_list:
                    product_name,price=i[0],i[1]
                    line=f"{product_name} {Spaces(28-len(product_name))} Rs.{price}\n"
                    bill_txt_area.insert(END,line)
                    total_line=f"\nTotal Tshirts Price : Rs.{Tshirt_price}\n{Spaces(90, '*')}\n"
                bill_txt_area.insert(END,total_line)
        if len(pants_list) > 0:
                bill_txt_area.insert(END, "Pants Product(s)\n\nProduct Name" + " " * 28 + "Price\n")
                for i in pants_list:
                    product_name, price = i[0], i[1]
                    line = f"{product_name} {Spaces(28 - len(product_name))} Rs.{price}\n"
                    bill_txt_area.insert(END, line)
                    total_line = f"\nTotal pants Price : Rs.{pants_price}\n{Spaces(90, '*')}\n"
                bill_txt_area.insert(END, total_line)
        if len(shoes_list)>0:
                bill_txt_area.insert(END,"Shoes Product(s)\n\nProduct Name"+" " * 28+"Price\n")
                for i in shoes_list:
                    product_name,price=i[0],i[1]
                    line=f"{product_name} {Spaces(28-len(product_name))} Rs.{price}\n"
                    bill_txt_area.insert(END,line)
                    total_line=f"\nTotal Shoes Price : Rs.{shoes_price}\n{Spaces(90, '*')}\n"
                bill_txt_area.insert(END,total_line)
        if len(Hoodie_list)>0:
                bill_txt_area.insert(END,"Hoodie Product(s)\n\nProduct Name"+" " * 28+"Price\n")
                for i in Hoodie_list:
                    product_name,price=i[0],i[1]
                    line=f"{product_name} {Spaces(28-len(product_name))} Rs.{price}\n"
                    bill_txt_area.insert(END,line)
                    total_line=f"\nTotal Hoodie Price : Rs.{Hoodie_price}\n{Spaces(90, '*')}\n"
                bill_txt_area.insert(END,total_line)
        if len(Jacket_list)>0:
                bill_txt_area.insert(END,"Jacket Product(s)\n\nProduct Name"+" " * 28+"Price\n")
                for i in Jacket_list:
                    product_name,price=i[0],i[1]
                    line=f"{product_name} {Spaces(28-len(product_name))} Rs.{price}\n"
                    bill_txt_area.insert(END,line)
                    total_line=f"\nTotal Jacket Price : Rs.{Jacket_price}\n{Spaces(90, '*')}\n"
                bill_txt_area.insert(END,total_line)
        bill_txt_area.insert(END,"\nTotal Price= Rs."+str(total_price))
        
        save_button=Button(root,relief="groove",text="Save Invoice",bg="green",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
        save_button.place(x=1120,y=600)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")

bill_gen_button=Button(root,text="Proceed to Checkout",font="times 17 bold",bg="white",fg="black",activebackground="purple",command=Bill)
bill_gen_button.place(x=1200,y=25)

root.mainloop()