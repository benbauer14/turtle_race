from turtle import Turtle, Screen

ben = Turtle("turtle")
june = Turtle("turtle")
max = Turtle("turtle")
ray = Turtle("turtle")
erica = Turtle("turtle")

ben.color("purple")
june.color("blue")
max.color("green")
ray.color("orange")
erica.color("red")

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Pick your horse (turtle)", "Which turtle will win the race? Enter a color:")
ben.penup()
ben.goto(-200, 150)
june.penup()
june.goto(-200, 75)
max.penup()
max.goto(-200, 0)
ray.penup()
ray.goto(-200, -75)
erica.penup()
erica.goto(-200, -150)


screen.exitonclick()