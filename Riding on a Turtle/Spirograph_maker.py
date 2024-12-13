import turtle
from turtle import Turtle, Screen
import random
cursor = Turtle()
cursor.color("black")
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
turtle.speed(10)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        cursor.color(random_color())
        cursor.circle(100)
        cursor.setheading(cursor.heading() + size_of_gap)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()