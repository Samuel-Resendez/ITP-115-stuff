# Author: Samuel Resendez
# ITP 115, Fall 2016
# Lab Practical L5
# saresend@usc.edu

# Get two sentences from the user
sentenceOne = input("Please enter a word or sentence: ")
sentenceTwo = input("Please enter a word or sentence: ")
# Make both of them lower case
sentenceOne = sentenceOne.lower()
sentenceTwo = sentenceTwo.lower()
#Remove Spaces
sentenceOne = sentenceOne.replace(" ", "")
sentenceTwo = sentenceTwo.replace(" ","")

#Convert srings to lsits
listOne = list(sentenceOne)
listTwo = list(sentenceTwo)
unsortListOne = listOne
unsortListTwo = listTwo
#Check if they are anagrams
print(listOne)
print(listTwo)
listOne.sort()
listTwo.sort()
if listOne == listTwo:
    print("They are anagrams!")
else:
    print("They are not anagrams!")
isListOnePalindrome = True
isListTwoPalindrome = True
reverseListOne = unsortListOne.reverse()
reverListTwo = unsortListTwo.reverse()
if unsortListOne != reverseListOne:
    isListOnePalindrome = False
if unsortListTwo != reverListTwo:
    isListTwoPalindrome = False
print("Is list one a palindrome? ", end = "")
print(isListOnePalindrome)
print("Is list two a palindrome? ", end = "")
print(isListTwoPalindrome)
