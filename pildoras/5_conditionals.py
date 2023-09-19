"""
Class 10: Conditionals part 1: Basics
Class 11: Conditionals part 2: elif usage
Class 12: Consitionals part 3: Concatenated comparison operators
Class 13: Conditionals part 4: Logic operators
Author: Eliana Chavez
"""


def quiz(score):
    status = "none"
    # 1 > score > 10
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


def validateScholarshipElegibility(distanceFromSchool, sibblings, annualSalary):
    eligibility = False

    if (distanceFromSchool > 40 and sibblings > 2) or annualSalary <= 20000:
        eligibility = True

    return eligibility


def selectOptativeSubjects(subject):
    # Warning!! Python is case sensitive
    subjects = ["Computer Science", "Math",
                "Communication", "Game Development"]
    if subject in subjects:
        print("You've been enrolled")
    else:
        print("Sorry", subject, "is not available")


def main():

    age = int(input("How old are you? "))

    if checkAge(age):
        validateAge(age)
    else:
        print("Invalid age")

    score = int(input("What was your exam score? "))
    print(quiz(score))

    print("Scholarship Elegibility Form")
    if validateScholarshipElegibility(
        int(input("How far do you live from school (km)? ")),
        int(input("How many siblings do you have? ")),
        int(input("How much money your family receive annually? "))
    ):
        print("You're elegible for the scholarship")
    else:
        print("Sorry, you're not elegible for the schoolarship")

    print("Choose optative subject")
    selectOptativeSubjects(input("What subject will you take? "))


main()
