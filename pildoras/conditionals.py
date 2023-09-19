"""
Class 10: Conditionals part 1
Class 11: Conditionals part 2
Class 12: Consitionals part 3
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


def checkAge(age):
    # Python evaluates conditions by pairs starting from left to right
    # 0 < age and age < 100
    if 0 < age < 100:  # Age must be positive and less than 100
        return True
    return False


def main():

    age = int(input("How old are you? "))

    if checkAge(age):
        validateAge(age)
    else:
        print("Invalid age")

    score = int(input("What was your exam score? "))
    print(quiz(score))


main()
