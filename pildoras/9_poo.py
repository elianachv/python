"""
Class 26: Class concepts
Class 27 - 28: Constructors, encapsulation
Class 29 - 31: Inheritance 
Author: Eliana Chavez
"""
# POO basics example


class Car():

    # Properties = Attributes (now in the constructor)

    # Constructor: Special method to specify initial status of the object
    # In python the contructor always has this structure and name
    def __init__(self):
        # Encapsulation: protect properties or methods adding __ to the atribute name
        self.__chasisLenght = 250
        self.__chasisWidth = 120
        self.__wheels = 4
        self.__agoing = False

    # Behavior = Methods
    # def for functions defs for methods (functions for a specific class)
    # self refers to the intance (the object itself) = this
    # In pyhton it's necessary to pass the self parameter

    def start(self):
        if self.__agoing:
            print("Car is already started")
        else:
            if self.__check():
                print("starting")
                self.__agoing = True
                print("started")
            else:
                print("Car cannot be started. Check it")

        return self.getStatus()

    def stop(self):
        if self.__agoing:
            print("stopping")
            self.__agoing = False
            print("stopped")
        else:
            print("Car is already stopped")

        return self.getStatus()

    def getStatus(self):
        if self.__agoing:
            return "Car is started"
        else:
            return "Car is stopped"

    def info(self):
        return f"""
              This car chasis is {self.__chasisLenght} length and {self.__chasisWidth} width
              It has {self.__wheels} wheels.
              Status: {self.getStatus()}
              """

    # Encapsulated method: it cannot be accessed outside the class
    def __check(self):
        print("Checking car status")
        self.fuel = "ok"
        self.oil = "low"
        self.doors = "closed"
        if self.fuel == "ok" and self.oil == "ok" and self.doors == "closed":
            return True
        else:
            return False


def pooExample():
    # Create instance of a class
    car = Car()
    car2 = Car()

    # Accessing attributes
    print("Try to modify number of wheels car 1")
    car.__wheels = 2  # Attribute won't be changed

    print(f"Car1: {car.info()}", f"Car2: {car2.info()}", sep="\n")

    # Calling methods
    print("Try to start car 1")
    car.start()
    print("Try to start car 1 again")
    car.start()
    print("Try to stop car 2")
    car2.stop()
    # car2.__check() # Generates error
    print(f"Car 1 status: {car.getStatus()}")
    print(f"Car 2 status: {car2.getStatus()}")

# Inheritance example


class Vehicle():

    def __init__(self, trademark, model, wheels):
        self.trademark = trademark
        self.model = model
        self.__wheels = wheels
        self.__agoing = False

    def start(self):
        if self.__agoing:
            print("Vehicle is already started")
        else:
            if self.__check():
                print("starting")
                self.__agoing = True
                print("started")
            else:
                print("Vehicle cannot be started. Check it")

        return self.getStatus()

    def stop(self):
        if self.__agoing:
            print("stopping")
            self.__agoing = False
            print("stopped")
        else:
            print("Vehicle is already stopped")

        return self.getStatus()

    def getStatus(self):
        if self.__agoing:
            return "Vehicle is started"
        else:
            return "Vehicle is stopped"

    def info(self):
        return f"""
              This vehicle:
              Trademark: {self.trademark}
              Model: {self.model}
              Number of wheels: {self.__wheels}
              Status: {self.getStatus()}
              """

    def __check(self):
        print("Checking car status")
        self.fuel = "ok"
        self.oil = "low"
        self.doors = "closed"
        if self.fuel == "ok" and self.oil == "ok" and self.doors == "closed":
            return True
        else:
            return False

# Class inherit from other


class Motorcycle(Vehicle):
    pass


def inheritanceExample():
    motorcycle1 = Motorcycle("Honda", "CBR", 2)
    print(motorcycle1.info())


def main():
    # pooExample()
    inheritanceExample()


main()
