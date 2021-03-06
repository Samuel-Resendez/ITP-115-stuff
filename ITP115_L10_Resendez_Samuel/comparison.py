#Author: Samuel Resendez
# ITP 115, Fall 2016
# Lab L10
# saresend@usc.edu

import time


def main():
    alphaList = readFile()
    printFreq(alphaList)


def readFile(filename="gettysburg.txt"):
    alpha = {}
    fileIn = open(filename, "r")
    for line in fileIn:
        line = line.strip()
        letterList = list(line)
        for letter in letterList:
            if letter not in " .,-\"\'?!":
                letter = letter.lower()
                if letter not in alpha:
                    alpha[letter] = 1
                else:
                    alpha[letter] += 1
    return alpha


def printFreq(freqDict):
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in alphabetList:
        if char in freqDict:
            print(char, end=": ")
            print(freqDict[char])










# ----- begin execution -----
main()
