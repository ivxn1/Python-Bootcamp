from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz : QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.question_canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125, text="question", fill='black', font=('Arial', 20, 'italic'), width=280)
        self.question_canvas.grid(row=1,column=0, columnspan=2, pady=20)

        tick_photo = PhotoImage(file='images/true.png')
        cross_photo = PhotoImage(file='images/false.png')

        self.tick_button = Button(image=tick_photo, highlightthickness=0, command=self.true_select)
        self.tick_button.grid(row=2, column=0, padx=20, pady=20)

        self.cross_button = Button(image=cross_photo, highlightthickness=0,command=self.false_select)
        self.cross_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_select(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_select(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(background="GREEN")
        else:
            self.question_canvas.config(background="RED")

        self.window.after(1000, func=self.get_next_question)

