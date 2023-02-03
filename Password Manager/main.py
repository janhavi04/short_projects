from tkinter import *
import math
import random

# Setting up screen:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Adding an icon:
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)

# Adding the logo:
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_manager_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)


generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()