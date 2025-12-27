from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    text = q['question']
    answer = q['correct_answer']
    question = Question(text, answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.user_score}/{len(question_bank)}.")