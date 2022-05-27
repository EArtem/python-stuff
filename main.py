from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


parameters = {
    'amount': 10,
    'type': 'boolean'
}


response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
json_data = response.json()

question_data = json_data['results']
print(question_data)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

