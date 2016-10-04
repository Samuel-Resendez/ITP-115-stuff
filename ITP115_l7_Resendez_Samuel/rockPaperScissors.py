# Author: Samuel Resendez
# ITP 115, Fall 2016
# Lab Practical L7
# saresend@usc.edu
#----- Imports -----
import random


def main():
    # ---- declare relevant vars -----
    userWantsToContinue = True
    playCounter = 0
    while userWantsToContinue:
        displayMenu()
        compChoice = getComputerChoice()
        humanChoice = getPlayerChoice()
        playCounter += playRound(compChoice,humanChoice)
        userWantsToContinue = continueGame()
    print("Your score was " + str(playCounter))
        



def getComputerChoice():
    computerInt = random.randrange(3)
    return computerInt

def getPlayerChoice():
    userInt = input("Please select 0 for Rock, 1 for Paper, and 2 for Scissors: ")
    while int(userInt) < 0 or int(userInt) > 2:
        userInt = input("Please select 0 for Rock, 1 for Paper, and 2 for Scissors: ")
    return int(userInt)
def playRound(computerChoice,userChoice):
    if computerChoice == userChoice:
        return 0
    elif computerChoice == 0 and userChoice == 2:
        return -1
    elif computerChoice == 1 and userChoice == 2:
        return 1
    elif computerChoice == 1 and userChoice == 0:
        return -1
    elif computerChoice == 0 and userChoice == 1:
        return 1
    elif computerChoice == 2 and userChoice == 0:
        return 1
    elif computerChoice == 2 and userChoice == 1:
        return -1

def displayMenu():
    print("Welcome! Let's play rock, paper, and scissors.")
    print("The rules of the game are as follows: ")
    print("\tRock smashes scissors")
    print("\tScissors cut paper")
    print("\tPaper covers rock")
    print("\tIf both choices are the same, its a tie")
def continueGame():
    print("Do you want to continue playing? Enter (y) for yes and (n) for no.")
    cont = input(">> ")
    if cont.lower() == "n":
        return False

if __name__ == "__main__":
    main()
