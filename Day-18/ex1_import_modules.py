from turtle import Turtle, Screen
# import turtle
# from turtle import Turtle as t

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("#f00")

# Square
# for _ in range(0, 4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# Dotted line
for _ in range(0, 10):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen = Screen()
screen.exitonclick()