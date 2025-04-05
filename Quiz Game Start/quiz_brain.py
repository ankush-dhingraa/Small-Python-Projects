class Quiz_brain:
    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
    
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1
        user = input(f"Q.{self.question_no} : {current_question.text}. (True/False)? :")
    
    def stil_has_questions(self):
        total_quiz_questions = len(self.question_list)
        if (self.question_no >= total_quiz_questions):
            return False
        else:
            return True
        