"""
Class 41: Save data permanently 
Author: Eliana Chavez
"""
import pickle


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self.age = age
        print("Person created ", self.name)

    def __str__(self) -> str:
        return "{} {} {}".format(self.name, self.age, self.gender)


def addPerson(personList, person):
    personList.append(person)


def showPeople(personList):
    for p in personList:
        print(p.__str__())


def getInfoFromFile():
    file = open("people-info", "ab+")
    file.seek(0)

    try:
        personList = pickle.load(file)
        print("Info was succesfully loaded. {} people were retrieved".format(
            len(personList)))
        showPeople(personList)
    except:
        print("File is empty")
    finally:
        file.close()
        del (file)


def createSampleData():
    p1 = Person("Mary", 23, "F")
    p2 = Person("Peter", 11, "M")
    p3 = Person("Mark", 45, "M")
    p4 = Person("Derek", 59, "M")

    personList = []
    addPerson(personList, p1)
    addPerson(personList, p2)
    addPerson(personList, p3)
    addPerson(personList, p4)

    showPeople(personList)

    return personList


def saveInfoInAFile(personList):

    file = open("people-info", "wb")

    try:
        pickle.dump(personList, file)
        print("Info was succesfully dumped into file")
    except:
        print("Unexpected error")
    finally:
        file.close()
        del (file)


def main():

    saveInfoInAFile(createSampleData())
    getInfoFromFile()


main()
