from tkinter import *
import random

# APP CONSTANTS:
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Card")


# Images and icons:

icon = PhotoImage(file="images/icon.png")
window.iconphoto(False, icon)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")


# Canvas:
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="French", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons:

unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)














window.mainloop()
