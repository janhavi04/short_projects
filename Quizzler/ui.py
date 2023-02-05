from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 15, "normal")


class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score card
        self.score_label = Label(text="Score:", fg="white", bg=THEME_COLOR, font=SCORE_FONT)
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Trial text", font=FONT, width=280,
                                                     fill=THEME_COLOR)
        # True/False Buttons:
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=3, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=3, column=1)
        # Icon:
        icon = PhotoImage(file="images/icon.png")
        self.window.iconphoto(False, icon)
        # Calls the next_question() from quiz_brain.
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_next = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_next)
