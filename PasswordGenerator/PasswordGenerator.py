from tkinter import *
import random, string
import pyperclip
from PIL import Image, ImageTk
import os

path = os.path.abspath('iu.png')

gui = Tk()
gui.geometry("400x200")
gui.resizable(0,0)
gui.title("Password Generator")

img = ImageTk.PhotoImage(Image.open(path))
gui.iconphoto(False, img)

Label(gui, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()

pass_label = Label(gui, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(gui, from_ = 15, to_ = 32 , textvariable = pass_len , width = 15).pack()

pass_str = StringVar()
def Generator():
    password = '' 

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(gui, text = "GENERATE PASSWORD" , command = Generator ).pack(pady = 5)

Entry(gui , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(gui, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

gui.mainloop()