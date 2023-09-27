"""
Class 39: Serialization part 1
Class 40: Serialization part 2
Author: Eliana Chavez
"""

import pickle

# Serialization is usefull to save data in databases or send it easily through internet


def serializeLists():
    names = ["Peter", "Isa", "Ana"]

    # wb = binary write
    binFile = open("names", "wb")

    # Save info into file
    pickle.dump(names, binFile)

    binFile.close()

    # Delete of memory
    del (binFile)


def readListFromBinFile():
    # rb = read binary
    file = open("names", "rb")
    names = pickle.load(file)
    print("List read from bin file: ", names)


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


def serializeObjects():

    v1 = Vehicle("Chevrolet", "Aveo", 4)
    v2 = Vehicle("Reanult", "Logan", 4)

    cars = [v1, v2]

    binFile = open("cars", "wb")

    pickle.dump(cars, binFile)

    binFile.close()

    del (binFile)


def readObjectsFromBinFile():
    # rb = read binary
    file = open("cars", "rb")
    cars = pickle.load(file)
    print("Object List read from bin file: ", cars)

    # Classof objetcs deserialized must be present in the file in order to work
    for c in cars:
        print(c.info())


def main():
    serializeLists()
    readListFromBinFile()
    serializeObjects()
    readObjectsFromBinFile()


main()
