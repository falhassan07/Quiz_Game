
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text}. (True/False): ")
        return user_answer

    
    def check_answer(self):
        pass


    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)



