from data import question_data
from question_model import Question

question_bank = []
for q_data in question_data:
    question_text = q_data["text"]
    question_answer = q_data["answer"]
    new_question_b = Question(question_text,question_answer)
    question_bank.append(new_question_b)

print(question_bank[0].text)
print(question_bank[0].answer)