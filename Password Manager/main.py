from tkinter import *
import math
import random




def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    data_to_add = f"\nWebsite: {website}, Email: {email}, Password: {password}"
    with open("data.txt", mode="a") as data_file:
        data_file.write(data_to_add)
    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')



# Setting up screen:

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Adding an icon:

icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)

# Canvas:

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_manager_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_manager_img)
canvas.grid(row=0, column=1)

# Labels:

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries:

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)
# Used for autofill purpose:

email_username_entry.insert(0, "sample_email@gmail.com")

password_entry = Entry(width=32,show="*")
password_entry.grid(row=3, column=1)

# Buttons:

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
