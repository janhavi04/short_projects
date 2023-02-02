from tkinter import *


def converter():
    miles = miles_input.get()
    km = str(round(float(miles) * 1.6, 2))
    kilometer_label.config(text=f"{km}")


window = Tk()
window.title("Miles to km convertor project.")
window.minsize(width=300, height=100)
# Padding
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(row=0, column=2)

miles_label = Label(text="    Miles")
miles_label.grid(row=0, column=3)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)
kilometer_label = Label(text="0")
kilometer_label.grid(row=1, column=2)
km_label = Label(text="Km")
km_label.grid(row=1, column=3)
calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(row=2, column=2)

window.mainloop()
