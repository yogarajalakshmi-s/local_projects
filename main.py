from data import question_data
from question_model import Question
from quiz import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))


quiz_obj = QuizBrain(question_bank)
while quiz_obj.still_has_questions():
    QuizBrain.next_question(quiz_obj)


print(f"Quiz is complete!\nYour final score is: {quiz_obj.score}/{len(question_bank)}")



# CREATING CLASS AND CLASS ATTRIBUTES AND METHODS
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.followers = 0 # Default attribute
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User('1', 'Yoga')
# user_2 = User('2', 'Ishu')
# # print(user_1.id, user_1.name)
# user_1.follow(user_2)
# print(f"USER - 1: {user_1.followers} {user_1.following}")
# print(f"USER - 2: {user_2.followers} {user_2.following}")
