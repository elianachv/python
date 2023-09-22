"""
Class 26: Class concepts
Author: Eliana Chavez
"""


class Car():

    # Properties = Attributes
    chasisLenght = 250
    chasisWidth = 120
    wheels = 4
    agoing = False

    # Behavior = Methods
    # def for functions defs for methods (functions for a specific class)
    # self refers to the intance (the object itself) = this
    # In pyhton it's necessary to pass the self parameter
    def start(self):
        if self.agoing:
            print("Car is already started")
        else:
          print("starting")
          self.agoing = True
          print("started")
    
    def getStatus(self):
        if self.agoing:
            return "Car is started"
        else:
            return "Car is stopped"


def main():
    # Create instance of a class
    car = Car()
    # Accessing attributes
    print(f"""
    This car chasis is {car.chasisLenght} length and {car.chasisWidth} width
    It has {car.wheels} wheels.
    {car.getStatus()}
    """
          )
    # Calling methods
    car.start()
    print (f"{car.getStatus()}")

main()
