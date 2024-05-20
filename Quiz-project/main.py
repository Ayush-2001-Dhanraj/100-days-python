from question_model import Question
from data import question_data

question_bank = [Question(data["text"], data["answer"]) for data in question_data]
