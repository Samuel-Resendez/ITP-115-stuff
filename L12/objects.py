#Author: Samuel Resendez
# ITP Lab 12 - 2016
# Lab practical L12
# saresend@usc.edu

# ---- imports ----
import random
###################

# ------ class definitions ----
class Die:

    mNumsides = 0
    mResult = 0
    
    def __init__(self,numSides=6):
        self.mNumsides = numSides

    def roll(self):
        self.mResult = random.randint(1,self.mNumsides)
    def __str__(self):
        return str(self.mResult)

# -------- function definitions ------
def main():
    valOne = 6
    valTwo = 6
    userInp = input("Do you want to use a default dice for your first dice(y/n)?: ")
    if userInp.lower() == "n":
        valOne = int(input("How many sides do you want? "))
    userInp = input("Do you want to use a default dice for your second dice?(y/n): ")
    if userInp.lower() == "n":
        valTwo = int(input("How many sides do you want? "))

    die1 = Die(valOne)
    die2 = Die(valTwo)
    die1.roll()
    die2.roll()
    print("Dice 1 rolled a " + str(die1.mResult) + ". Dice 2 rolled a " + str(die2.mResult))
    print("The Sume of Dice 1 and Dice 2 is " + str(findSum(die1.mResult, die2.mResult)))

def findSum(dieNum1,dieNum2):
    return dieNum1 + dieNum2

# -------- begin execution ---------
main()
