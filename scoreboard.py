from turtle import Turtle
FONT = ('Courier', 15, 'normal')
ALIGNMENT = 'center'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score_file.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.print_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('Game Over!', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_file.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # (or) data.write(str(self.high_score))
        self.score = 0
        self.print_score()
