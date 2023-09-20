"""
Class 14: Loops part 1: For basics
Class 15: Loops part 2: For
Class 16: Loops part 3: range and print tips
Class 17: Loops part 4: While
Class 18: Lopps part 5: continue, pass and else
Author: Eliana Chavez
"""
import math

# Determined loops : for
# range(n) could be a list, a tuple, a string, etc
# Default range(stop)

def printForSamples():
    print("Printing 5 times Hello world")
    for i in range(5):
        print("Hello world!", sep="", end=" ")

    print("\n")

    # range(start,stop,step)
    print("Printing 2 times Hello world using range")
    for i in range(1, 3, 1):
        print(f"Hello world! {i}")

    print("\n")

    print("Printing names in a list")
    for name in ["Isaboth", "Ichimei", "Eli"]:
        print("Hello", name)

    print("\n")


def validateEmail(email):

    emailSyntax = False
    emailTermination = False
    count = 0

    for i in email:

        if i == "@" or i == ".":
            count += 1

    if count >= 2:
        emailSyntax = True

    for i in (".com", ".es", ".co", ".net"):
        if str(email).__contains__(i):
            emailTermination = True

    return emailSyntax and emailTermination


def printEmailValidation(email):

    print("Validate email")
    if validateEmail(email):
        print(email, "is ok")
    else:
        print(email, "is invalid")


def executeEmailExampleFor():

    print("Email validation sample results")
    for email in ("test@gmail.com", "testgmail.com", "test@gamail", "test"):
        printEmailValidation(email)
        print("\n")

    print("Email validation test")
    printEmailValidation(input("What's your email? "))

# Undetermined loops : while


def printWhileSamples():
    i = 1
    while i <= 10:
        print("Execution", i)
        i += 1

    age = int(input("How old are you? "))
    while 0 < age < 100:
        print("Valid age", age)
        age = int(input("How old are you? "))

    print("Thanks")


def calculateSqureRootWhile():
    attempt = 0
    number = int(input("Digit number: "))

    while number < 0:
        print("Error, square root cannot be calculated for negative values")

        if attempt == 2:
            print("You've have tried so many times")
            break

        number = int(input("Digit number: "))
        if number < 0:
            attempt += 1

    if attempt < 2:
        solution = math.sqrt(number)
        print(f"square root of {number} is {solution}")

# continue: ignore the rest of the loop code and jump to the next iteration
# pass: return null, do not execute the loop example: defining classes
# else: execute something if for ends completely


def continueExamples():
    print("\nPrinting letters example:")
    for letter in "python":

        if letter == "h":  # h won't be printed
            continue

        print("Letter:", letter)

    print("\nCounting letters example:")
    count = 0
    phrase = "This is a long test"
    for letter in phrase:

        if letter == " ":  # spaces wont be counted
            continue

        count += 1

    print("Whole size:", len(phrase))
    print("Char count:", count)


def passExample():
    # Wait till user press ctrl + C
    while True:
        pass


def elseExample():
    email = input("What's your email? ")

    for i in email:
        if i == "@":
            at = True
            break

    else: 
        at = False

    print("@ is present: ", at)


def main():
    # printForSamples()
    # executeEmailExampleFor()
    # printWhileSamples()
    # calculateSqureRootWhile()
    # continueExamples()
    # passExample()
    elseExample()


main()
