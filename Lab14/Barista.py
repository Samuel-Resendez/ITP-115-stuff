#Author: Samuel Resendez
# ITP 115 - Lab 14
# saresend@usc.edu

#------ imports ---------
from Coffee import Coffee


class Barista(object):
    maxOrders = 5

    def __init__(self,name):
        self.__name = name
        self.__orders = []

    def takeOrder(self):
        print("Hello, my name is",self.__name,"what would you like today?")
        customer = input("What is your name?: ")
        size = input("What size would you like? ")
        drink = input("What drink do you want? ")
        order = Coffee(size,drink,customer)
        self.__orders.append(order)
        print(order)

    def isAcceptingOrders(self):
        if len(self.__orders) >= Barista.maxOrders:
            return False
        else:
            return True
    def makeDrinks(self):
        for coffee in self.__orders:
            coffee.setCompleted()
            print(coffee)
        self.__orders = []

    def __str__(self):
        return "Hi my name is,",self.__name
    
