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

#defining function to hide all frames inside product frame
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()

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

pants_button=Button(Button_frame,text="Pants",font="times 20 bold",command=pantsCall)
pants_button.grid(row=0,column=0,padx=10,pady=10)
Tshirt_button=Button(Button_frame,text="Tshirt",font="times 20 bold",command=TshirtCall)
Tshirt_button.grid(row=1,column=0,padx=10,pady=10)

root.mainloop()