from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.size()
window.title("Pomodoro App")
window.config(padx=100, pady=50)
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)


canvas = Canvas(width=200, height=224)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=pomodoro_img)
canvas.pack()

window.mainloop()
