from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        file = open("data.txt")
        self.high_score = int(file.read())
        self.game_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        file.close()

    def update_scoreboard(self):
        self.clear()
        if self.high_score  > self.game_score:
            s = self.high_score
        else:
            s = self.game_score
        self.write(f"Score: {self.score}  High Score: {s}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score  > self.high_score:
            with open("data.txt","w") as file:
                file.write(str(self.score))
            if self.score > self.game_score:
                self.game_score = self.score

        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
