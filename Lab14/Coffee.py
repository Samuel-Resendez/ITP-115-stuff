#Author: Samuel Resendez
# ITP 115 - Lab 14
# saresend@usc.edu


class Coffee(object):
    statuses = ["ordered","completed"]
    def __init__(self,size,desc,cust):
        self.__size = size
        self.__description = desc
        self.__customer = cust
        self.__status = 0
    def setCompleted(self):
        self.__status = 1

    def __str__(self):
        str = "A "+ self.__size + " " + self.__description + " for " + self.__customer + " ("+Coffee.statuses[self.__status]+")"
        return str

