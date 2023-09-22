#!/bin/python3

print("Hi, Welcome to the coffe shop")
name = input("What's your name? ")

menu = (
"""
______________________________________________
                    MENU
______________________________________________
    1. Coffe
    2. Tea
    3. Water
_______________________________________________
"""
)

price = 4
print("Hi ",name," check out our menu\n", menu)
option = input("What would you like to order? ")
units = int(input("How many units dou you want? "))
print("Your",option,"will be ready in a moment ")
print("Total cost:", str(price * units),"USD")

