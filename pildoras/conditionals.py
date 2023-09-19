"""
Class 10: Conditionals part 1
Class 11: Conditionals part 2
Author: Eliana Chavez
"""

def quiz(score):
    status = "none"
    if score > 10 or score < 1:
        status = "Invalid score"
        return
    if score > 7:
        status = "approved"
    else:
        status = "failed"
    return status


def validateAge(age):
    if age >= 65:
        print("You're an elder")
    elif (age >= 30 and age < 65):
        print("You're an adult")
    elif (age >= 18 and age < 30):
        print("You're a teen")
    else:
        print("You're a kid")


def main():

    age = int(input("How old are you? "))
    validateAge(age)

    score = int(input("What was your exam score? "))
    print(quiz(score))


main()
