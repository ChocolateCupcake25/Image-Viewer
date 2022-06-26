# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 09:12:30 2022

@author: HP
"""

from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog

root= Tk()
root.title(" IMAGE_VIEWER")
root.geometry("500x500")
root.configure(bg="medium slate blue")

lable_image=Label(root, bg="misty rose",highlightthickness=5,borderwidth=2,relief=SOLID)
lable_image.place(relx=0.5,rely=0.5,anchor=CENTER)

img_path=""
def OpenImage():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image Files", filetypes= [("Image Files", "*.jpg; *.gif; *.png; *.jpeg;*txt")])
    print(img_path)
    img=ImageTk.PhotoImage(Image.open(img_path))
    lable_image["image"]=img
    img.close()
    
def RotateImage():
    global img_path
    im = Image.open(img_path)
    rotated_img=im.rotate(180)
    img=ImageTk.PhotoImage(Image.open(rotated_img))
    lable_image["image"]=img
    img.close()
    

openImage=Button(root,text="Open Image", command=OpenImage,bg="lightSalmon2",font=("castellar",10,"bold"),relief=RIDGE,borderwidth=5)
openImage.place(relx=0.5,rely=0.1,anchor=CENTER)

rotateImage=Button(root,text="Rotate Image",command=RotateImage,bg="lightSalmon2",font=("castellar",10,"bold"),relief=RIDGE,borderwidth=5)
rotateImage.place(relx=0.5,rely=0.8,anchor=CENTER)

label=Label(root,text="Created by:Ziyah ",bg="medium slate blue")
label.place(relx=0.5,rely=0.95,anchor=CENTER)

root.mainloop()
