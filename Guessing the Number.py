import turtle
turtle.penup()
turtle.hideturtle()
turtle.goto(-357,0)
turtle.left(90)
turtle.forward(313)
turtle.right(90)
turtle.forward(357)
turtle.write("Guessing the Number", font=("Arial", 23, "bold"), align="center")
turtle.right(90)
turtle.forward(17)
turtle.write("Game Instructions", font=("Arial", 16), align="center")
turtle.forward(17)
turtle.write("Your task is to guess the correct number between 1 and 10 within 10 tries.", font=("Arial", 16), align="center")
turtle.forward(15)
turtle.write("However, there's a twist!", font=("Arial", 16), align="center")
turtle.forward(15)
turtle.write("If you guess correctly, you'll see a green background, otherwise, you'll see a red background.", font=("Arial", 16), align="center")
turtle.forward(15)
turtle.write("Once you've done 10 tries, you'll know if you won or not.", font=("Arial", 16), align="center")
turtle.forward(15)
turtle.write("Good luck and let's get started!", font=("Arial", 16), align="center")
turtle.forward(50)
import time
score=0
for i in range(1,11):
    import random
    comp=random.randint(1,10)
    comp=int(comp)
    num=turtle.textinput("Enter your guess:", "Pick 1 to 10:")
    num=int(num)
    if comp==num:
        bg=turtle.Screen()
        bg.bgcolor("green")
        time.sleep(1)
        bg.bgcolor("white")
        score=score+1
    else:
        bg=turtle.Screen()
        bg.bgcolor("red")
        time.sleep(1)
        bg.bgcolor("white")
if score>=7:
    turtle.write(format(score)+"/10 - you're the winner!", font=("Arial", 16), align="center")
else:
    turtle.write(format(score)+"/10 - it's ok, next time you'll win!", font=("Arial", 16), align="center")
time.sleep(5)
turtle.Screen().bye()
