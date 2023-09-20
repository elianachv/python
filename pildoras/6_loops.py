"""
Class 14: Loops part 1: For basics
Class 15: Loops part 2: For
Author: Eliana Chavez
"""

# Determined loops : for
# range(n) could be a list, a tuple, a string, etc

print("Printing 5 times Hello world")
for i in range(5):
    print("Hello world!", sep="", end=" ")

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


print("Email validation sample results")
for email in ("test@gmail.com", "testgmail.com", "test@gamail", "test"):
    printEmailValidation(email)
    print("\n")


print("Email validation test")
printEmailValidation(input("What's your email? "))
