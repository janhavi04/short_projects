from tkinter import *
import math

# APP CONSTANTS:
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def start_timer():
    count_down(12)


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


window = Tk()
window.size()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)

# Timer label:

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

# Pomodoro countdown and image:

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Operations buttons:

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=3, column=2)

# Check marks:

check_label = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(row=4, column=1)

window.mainloop()
