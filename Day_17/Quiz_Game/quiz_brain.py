class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.user_score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)?: ")
        self.check_answer(user_answer, current_q.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, act_answer):
        if u_answer.lower() == act_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("Nope. That's wrong!")
        print(f"The right answer was: {act_answer}.")
        print(f"Your current score is {self.user_score}/{self.question_number}!")
        print()



