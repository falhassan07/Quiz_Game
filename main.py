from question_model import Question
from quiz_brain import QuizBrain
from data import get_data
import html



question_bank = []

data = get_data()
for item in data:
    question = html.unescape(item["question"])
    answer = item["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()