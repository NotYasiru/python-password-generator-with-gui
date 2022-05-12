from ast import Pass
from cgitb import text
from logging import root
from sqlite3 import Row
from tkinter import *
from tkinter import font
from turtle import color
from random import randint
from tkinter import messagebox

root = Tk()

root.title("Password Generator")
width = (root.winfo_screenwidth()) / 3
height =(root.winfo_screenheight()) / 3
root.geometry("%dx%d" % (width, height))
root.resizable(False,False)
root.iconbitmap("icon_v2.ico")

ltopic = Label(root, text="Password Generator", font='arial 42 bold', pady=5).pack()

def new_rand():
    pw_entry.delete(0,END)

    if pswd_len.get() == '' or pswd_len.get() == '0':
        messagebox.showerror("Error", "Please Enter how many characters you want")
    
    else:
        pw_len = int(pswd_len.get())
    
        password = ''

        for x in range(pw_len):
            password += chr(randint(33, 126))
    
        pw_entry.insert(0, password)


def copybtn():
    if pswd_len.get() == '' or pswd_len.get() == '0':
        messagebox.showerror("Error", "Please Enter how many characters you want")
    else:
        root.clipboard_clear()
        root.clipboard_append(pw_entry.get())
        messagebox.showinfo("Info", "Copied to clipboard")

lf = LabelFrame(root, text="How many Characters? ", font=('arial', 12))
lf.pack(pady=20)

pswd_len = Entry(lf, font=('Helvetica', 24))
pswd_len.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=('Helvetica', 24), bd=0, bg='systembuttonface')
pw_entry.pack(pady=10)

my_frame = Frame(root)
my_frame.pack(pady=15)

gen_pwd = Button(my_frame, text="Generate Password", command=new_rand, font=('Arial', 12), padx=5, pady=5)
gen_pwd.grid(row=0, column=0, padx=8)

clip_button = Button(my_frame, text="Copy to Clipboard", command=copybtn, font=('Arial', 12), padx=5, pady=5)
clip_button.grid(row=0, column=1, padx=8)

root.mainloop()
