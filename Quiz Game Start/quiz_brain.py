class Quiz_brain:
    def __init__(self,q_list):
        self.question_no = 0
        self.question_list = q_list
    
    def next_question(self):
        user = input(f"Q {self.question_no +1} : {self.next_question[self.question_no].text} (True/False)? :")
        self.question_no +=1
