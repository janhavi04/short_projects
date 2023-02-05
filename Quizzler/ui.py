from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface():
    def __init__(self):

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:", fg="white", bg=THEME_COLOR, justify= RIGHT)
        self.score_label.grid(row=0, column=1, ipady=20)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.create_text(150, 125, text="Trial text", font=FONT)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=3, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=3, column=1)
        icon = PhotoImage(file="images/icon.png")
        self.window.iconphoto(False, icon)


        self.window.mainloop()

