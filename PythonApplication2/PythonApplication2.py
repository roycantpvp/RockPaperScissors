#rockpaperscissors
import math
from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)] #generators random number between 0 -2
player = False 

while player == False:
#set player to True
    player = input("Rock, Paper, or Scissors?: ")
    if player == computer:
        print("Tie!")   #Tie case
    elif player == "Rock":     #Rock case
        if computer == "Paper":
            print("You lost!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper": #Paper Case
        if computer == "Scissors":
            print("You lost!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors": #Scissor case
        if computer == "Rock":
            print("You lost...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else: #Error/mistype case
        print("That's not a valid play. Check your spelling!")
    #Runs the game back
    player = False
    computer = t[randint(0,2)]