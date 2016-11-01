# Author: Samuel Resendez
# ITP 115 - Assignment 9
# saresend@usc.edu
# Cheers!

#---- imports ----
from Superhero import Superhero


# ---- method declaration -----
def main():
    userWantsToContinue = "y"
    while(userWantsToContinue != "n"):
        fighterOneName = input("Enter fighter #1's name: ")
        fighterOneType = input("Is figheter #1 a hero or a villain?: ")
        fighterOneAtk = int(input("Enter fighter #1's attack points: "))
        fighterTwoName = input("Enter superhero #2's name: ")
        fighterTwoType = input("Is fighter #2 a hero or villain?: ")
        fighterTwoAtk = input("Enter fighter #2's attack points: ")
        fighterOne = Superhero(fighterOneName,fighterOneType,fighterOneAtk)
        fighterTwo = Superhero(fighterTwoName,fighterTwoType,fighterTwoAtk)
        print("FIGHTERS")
        print("")
        print("")
        print(fighterOne)
        print(fighterTwo)
        print("")
        print("BEGINNING BATTLE!")
        print("")
        numRounds = 1
        while(not fighterOne.isDead() and not fighterTwo.isDead()):
            print("============ Round",str(numRounds),"==============")
            fightOne.loseHealth(fighterTwo.getAttack())
            fighterTwo.loseHealth(fighterOne.getAttack())
            print(fighterOne)
            print(fighterTwo)
        if(fighterOne.isDead() and fighterTwo.isDead()):
            print("Tie. Both died.")
        elif(fighterOne.isDead()):
            print(fighterTwo.name,"won!")
        else:
            print(fighterOne.name,"won!")
        userWantsToContinue = input("Would you like to play again?(y/n): ")


#-------begin execution ----
main()
