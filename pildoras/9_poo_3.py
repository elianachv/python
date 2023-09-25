"""
Class 32: Polymorphism
Author: Eliana Chavez
"""


class Car():
    def info(self):
        return "I'm a car"


class Bike():
    def info(self):
        return "I'm a bike"


class Van():
    def info(self):
        return "I'm a van"


class Motorcycle():
    def info(self):
        return "I'm a motorcycle"


# In this function we can change the behavior of a the param vehicle so we can see polymorphism in action
def info(vehicle):
    print(vehicle.info())


def main():

    vehicle1 = Car()
    vehicle2 = Bike()
    vehicle3 = Van()

    vehicles = [vehicle1, vehicle2, vehicle3]

    for v in vehicles:
        info(v)


main()
