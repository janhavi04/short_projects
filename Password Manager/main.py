from tkinter import *
import math
import random

# Setting up screen:
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Adding an icon:
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)

# Adding the logo:
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_manager_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager_img)
canvas.grid(row=1, column=1)











window.mainloop()