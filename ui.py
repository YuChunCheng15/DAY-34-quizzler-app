from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightbackground=THEME_COLOR)
        self.question_text = self.canvas.create_text(150, 125, width=280 ,text="Some Question", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", font=("Arial", 16), bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=right_img, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.right.grid(column=0, row=3,)
        wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_img, highlightbackground=THEME_COLOR,command=self.false_pressed)
        self.wrong.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

