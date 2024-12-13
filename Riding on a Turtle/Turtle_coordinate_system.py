from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400)
text_bet = screen.textinput(title = "Make your bet !", prompt = "Who are you betting on, enter a color (vibgyor): ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_index = [-150, -100, -50, 0, 50, 100, 150]
shape = []
all_turtles = []

for i in range(7):
    tim = Turtle(shape = "turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x = -230, y = y_index[i])
    tim.pendown()
    all_turtles.append(tim)

if text_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color != text_bet:
                print(f"You've lost, {win_color} turtle aced")
            else:
                print(f"You've won, {win_color} turtle aced")
        dist = random.randint(1, 10)
        turtle.forward(dist)
screen.exitonclick()
