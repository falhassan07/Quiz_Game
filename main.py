from question_model import Question
from quiz_brain import QuizBrain
from data import get_data
from ui import QuizInterface
import html



question_bank = []

data = get_data()
for item in data:
    question = html.unescape(item["question"])
    answer = item["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)




quiz = QuizBrain(question_bank)
quiz_Ui = QuizInterface(quiz)
