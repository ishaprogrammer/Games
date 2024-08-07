class QuizBrain():
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"Q.{self.question_number}:{current_question.text} (True/False)")
        self.check_answer(answer,current_question.answer)
    def still_has_question(self):
        return self.question_number<len(self.question_list)
    def check_answer(self,answer,coreect_answer):
        if answer.lower()==coreect_answer.lower():
            print("correct")
            self.score+=1
        else:
            print("wrong")
        print(f"correct answer is {coreect_answer}")
        print(f"score:{self.question_number}/{self.score}")
    
        
        
        