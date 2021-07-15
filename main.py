from turtle import Turtle, Screen
import random

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
user_bet = screen.textinput("Pick your horse (turtle)", "Which turtle will win the race? Enter a color:").lower()
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
winner = False
while winner == False:
    ben.goto(ben.xcor() + random.randint(2, 15), ben.ycor())
    june.goto(ben.xcor() + random.randint(2, 15), june.ycor())
    max.goto(ben.xcor() + random.randint(2, 15), max.ycor())
    ray.goto(ben.xcor() + random.randint(2, 15), ray.ycor())
    erica.goto(ben.xcor() + random.randint(2, 15), erica.ycor())
    if(ben.xcor() >= 225):
        winner = True
        if(user_bet == 'purple'):
            print("You win! Purple won the race!")
        else:
            print("You lose! Purple won the race!") 
    elif(june.xcor() >= 225):
        winner = True
        if(user_bet == 'blue'):
            print("You win! Blue won the race!")
        else:
            print("You lose! Blue won the race!")  
    elif(max.xcor() >= 225):
        winner = True
        if(user_bet == 'green'):
            print("You win! Green won the race!")
        else:
            print("You lose! Green won the race!")  
    elif(ray.xcor() >= 225):
        winner = True
        if(user_bet == 'orange'):
            print("You win! Orange won the race!")
        else:
            print("You lose! Orange won the race!")  
    elif(erica.xcor() >= 225):
        winner = True
        if(user_bet == 'red'):
            print("You win! Red won the race!")
        else:
            print("You lose! Red won the race!")


screen.exitonclick()