class Quiz_brain:
    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
    
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1
        user_answer = input(f"Q.{self.question_no} : {current_question.text}. (True/False)? :")
    
    def stil_has_questions(self):
        return self.question_no < len(self.question_list)
    def check_answer(self,user_aswer,correct_answer):
        if user_aswer.lower() == correct_answer.lower():
            print("You got it Right!")
        else:
            print("That's wrong")