"""
Class 19: Generators part 1: basics
Class 20: Generators part 2: yield from
Author: Eliana Chavez
"""

# Generators return values one by one
# They're more efficient, useful with infinite lists


def generateNumbersFunction(limit):
    num = 1
    numberList = []

    while num < limit:
        numberList.append(num * 2)
        num += 1

    return numberList


def generateNumbersGenerator(limit):
    num = 1

    while num < limit:
        yield num * 2
        num += 1


def functionsVsGeneratorExample():
    # For use a function you just call it once
    print("Result with function", generateNumbersFunction(8))

    # For use a generator you must use a loop to iterate it or the next() function
    # Generator build the next result in each call optimize resources
    print("Result total with generator")
    result = generateNumbersGenerator(10)
    print("Call fisrt result generator", next(result))
    for i in result:
        print(i)


# Generator for elements with elements
# The * before a parameter means undetermined number of params
def generateCities(*cities):
    for city in cities:
        yield city


# Accesing each letter of each city
def generateCitiesLetterByLetter(*cities):
    for city in cities:
        for letter in city:
            yield letter


# Accesing each letter of each city simplify
def generateCitiesLetterByLetterV2(*cities):
    for city in cities:
        yield from city


def generatorForElementsWithElementsExsample():
    print("\nTraditional generator")
    cities = generateCities("Bogota", "Lima", "Madrid", "Barcelona")

    print(next(cities))
    print(next(cities))

    print("\nSubelement generator")
    letters = generateCitiesLetterByLetter("Bogota", "Lima", "Madrid", "Barcelona")

    print(next(letters))
    print(next(letters))

    print("\nSubelement generator v2")
    letters_v2 = generateCitiesLetterByLetterV2("Bogota", "Lima", "Madrid", "Barcelona")

    print(next(letters_v2))
    print(next(letters_v2))


def main():
    # functionsVsGeneratorExample()
    generatorForElementsWithElementsExsample()


main()
