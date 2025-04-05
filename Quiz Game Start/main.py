from data import question_data
from question_model import Question
from quiz_brain import Quiz_brain

question_bank = []
for q_data in question_data:
    question_text = q_data["text"]
    question_answer = q_data["answer"]
    new_question_b = Question(question_text,question_answer)
    question_bank.append(new_question_b)

quiz = Quiz_brain(question_bank)

while quiz.stil_has_questions():
    quiz.next_question()
print("You've completed quiz!")
print(f"Your final score was :{quiz.score}/{quiz.question_no}")