from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(data["question"], data["correct_answer"]) for data in question_data]

quiz = QuizBrain(question_bank)

while quiz.has_question():
    quiz.next_ques()

print(f"You've completed the Quiz.\nYour final score is: {quiz.score}/{len(quiz.question_list)}")
