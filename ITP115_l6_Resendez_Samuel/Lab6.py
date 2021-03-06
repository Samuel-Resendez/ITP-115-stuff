

# Author: Samuel Resendez
# ITP 115, Fall 2016
# Lab Practical L6
# saresend@usc.edu


# - Boilerplate - 
import random

#----- method declarations ----


# -- variables and such -- 
choice = 0
articles = ["a","the"]
nouns = ["person","place","thing"]
verbs = ["danced","ate","frolicked"]


# -- begin execution -- 
print("Welcome to the Sentence Generator! Would you like to?")
while choice != "5":
    print("1) View Words")
    print("2) Add Words")
    print("3) Remove Words")
    print("4) Generate Sentence")
    print("5) Exit")
    choice = input(">> ")
    if choice == "1":
        print(articles)
        print(nouns)
        print(verbs)
    elif choice == "2":
        print("Would you like to add 1) articles, 2) verbs, or 3) nouns?")
        verbOrNoun = input(">> ")
        if verbOrNoun == "1":
            article = input("Enter article to add: ")
            articles.append(article)
        elif verbOrNoun == "2":
            verb = input("Enter verb to add: ")
            verbs.append(verb)
        elif verbOrNoun == "3":
            noun = input("Enter noun to add: ")
            noun.append(noun)
    elif choice == "4":
        sentence = ""
        for int in range(0,2):
            article = random.choice(articles)
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            sentence += article + " " + noun + " " + verb + " "
        print(sentence)
    elif choice == "5":
        print("Thank you for your time")
        break;
    else:
        print("Pick a valid input")
        continue


