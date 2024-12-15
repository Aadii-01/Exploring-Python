from turtle import Turtle
class Paddle(Turtle):
    def __init__ (self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 10
        if new_y > 240:
            new_y -= 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        if new_y < -230:
            new_y += 10
        self.goto(self.xcor(), new_y)