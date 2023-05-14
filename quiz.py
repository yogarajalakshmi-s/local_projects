class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"{self.question_num}. {question.text} (True/False): ")
        correct_answer = question.answer
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        total_questions = len(self.question_list)
        return total_questions > self.question_num

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong!")
        print(f"Correct answer is: {correct_answer}\nSCORE: {self.score}/{self.question_num}\n")
