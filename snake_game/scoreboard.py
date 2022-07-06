from food import Food

class Score(Food):

    def __init__(self):
        super().__init__()
        self.goto(0,250)
        self.score = 0
        self.high_score = 0
        with open("new.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("new.txt", mode="w") as file:
            file.write(f"{self.high_score}")



