#create a rock, paper, scissors game
#rock = 1, scissors = 2, paper = 3
import random
#the computer chooses between 1-3
comp = random.randint(1,3)
comp = int(comp)
#ask the users for their choice
user = input("Rock, scissors, or paper? ")
print("You pick a "+user)

#Create an if statement for the computer
if comp == 1:
    comp = "rock"
elif comp == 2:
    comp = "scissors"
else:
    comp = "paper"
print("Computer picks "+comp)

#print out the winner
if comp == user:
    print("Tie!")
elif comp == "rock" and user == "paper":
    print("You did it!")
elif comp == "paper" and user == "rock":
    print("Computer won!")
elif comp == "rock" and user == "scissors":
    print("Computer won!")
elif comp == "scissors" and user == "rock":
    print("You did it!")
elif comp == "paper" and user == "scissors":
    print("You did it!")
else:
    print("Computer won!")
