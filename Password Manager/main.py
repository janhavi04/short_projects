from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            password = data[website]["Password"]
            email = data[website]["Email"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message="No details for the website exists.")


def save():
    website = website_entry.get().strip()
    email = email_username_entry.get()
    password = password_entry.get()
    data_dict = {
        website: {
            "Email": email,
            "Password": password,
        },
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields", message="You have left certain fields empty.")
    else:
        confirmation = messagebox.askokcancel(title=website, message=f"Details entered:\nEmail: {email}\n"
                                                                     f"Password: {password}\nDo you want to save?")

        if confirmation:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(data_dict, data_file, indent=4)
            else:
                data.update(data_dict)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
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

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons:

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()



