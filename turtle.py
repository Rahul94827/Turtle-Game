from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color: ")
colors=["Red","Blue","Green","Brown","Orange","Yellow"]
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]
is_bet=False
line=Turtle()
line.setheading(39)
line.penup()
line.forward(300)
line.setheading(270)
line.pendown()
line.forward(390)
line.hideturtle()

for pos in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[pos])
    new_turtle.goto(x=-230, y=y_pos[pos])
    all_turtle.append(new_turtle)


if user_bet:
    is_bet=True

while is_bet:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_bet=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won,The {winning_color} turtle is the winner")
            else:
                print(f"You lost,The {winning_color} turtle is the winner")


        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
