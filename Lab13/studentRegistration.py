#Author: Samuel Resendez
# ITP 115 - Fall 2016
# Lab 13
# saresend@usc.edu
# Cheers!!


#----- begin class implementations -----

#---- global vars ---
MAX_CLASSES = 6

class Student:
    # attributes
    def __init__(self,studentName,studentIDNumber):
        self.__name = studentName
        self.__idNumber = studentIDNumber
        self.__numberOfClasses = 0
        self.__classes = []

    def getName(self):
        return self.__name
    def setName(self,newName):
        self.__name = newName
    def getID(self):
        return self.__idNumber
    def setID(self,idNumbah):
        self.__idNumber = idNumbah
    def getNumberOfClasses(self):
        return self.__numberOfClasses
    def addClass(self,nameOfClass):
        if self.__numberOfClasses < MAX_CLASSES:
            self.__classes.append(nameOfClass)
            return True
        else:
            return False
    def __str__(self):
        string = "Student: " + self.__name + "\n"
        string+= "ID Number: " + str(self.__idNumber) + "\n"
        string += "Enrolled in: " + str(self.__numberOfClasses) + " classes." + "\n"
        string += str(self.__classes)
        return string

# ------- method declarations --------
def printStudents(studentList):
    print("Students: ")
    counter = 1
    for student in studentList:
        print(str(counter)+")",end="")
        print("\t" + student.getName())
        counter += 1

def main():
    student1 = Student("Mark",1678)
    student2 = Student("Neil",942)
    student3 = Student("Stiven",254)
    student4 = Student("Samuel",981)
    studentList = [student1,student2,student3,student4]
    print("Welcome to the student registration system")
    userWantsToContinue = True
    userInput = 0
    while(userWantsToContinue):
        print("Please select a student from the list")
        printStudents(studentList)
        userInput = int(input("Please make a selection: "))
        classToRegister = input("Enter a class the student is registering for: ")
        wasSuccessful =studentList[userInput-1].addClass(classToRegister)
        if wasSuccessful:
            print("Class was successfully added!")
        else:
            print("Failed to add class :(")
        userDesire = input("Would you like to continue registering?(y/n) ")
        if userDesire.lower() == "n":
            userWantsToContinue = False

main()
