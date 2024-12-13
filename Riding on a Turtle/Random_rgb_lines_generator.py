import turtle
from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.color("black")
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
directions = [0 , 90 , 180 , 270]
timmy_the_turtle.pensize(15)
for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()