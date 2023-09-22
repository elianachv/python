"""
Class 21: Exceptions part 1: basics
Class 22: Exceptions part 2: finally clause
Class 23: Exceptions part 3: throw exceptions intentionally
Author: Eliana Chavez
"""
# Exceptions are usually managed with try excepts blocs


def divide(num1, num2):
    try:
        if isinstance(num1, int) == False:
            num1 = int(num1)

        if isinstance(num2, int) == False:
            num2 = int(num2)

        return num1 / num2

    except ZeroDivisionError:
        print("Division by zero is not allowed")
        return "infinite"
    except ValueError:
        print("Invalid values were entered")
        return "error"
    except Exception:
        print("Unexpected error")
        return "error"


def divideApp():
    num1 = input("Digit number 1: ")
    num2 = input("Digit number 2: ")
    result = 0
    try:
        if isinstance(num1, int) == False:
            num1 = int(num1)

        if isinstance(num2, int) == False:
            num2 = int(num2)

        result = num1 / num2

    except ZeroDivisionError:
        print("Division by zero is not allowed")
        result = "infinite"
    except ValueError as InavlidValues: # Create custom names for generic exceptions
        print("Invalid values were entered")
        result = "error"
    except:  # It's not a good practice, cause we cannot give a good feedback to the user
        print("Unexpected error")
        result = "error"
    finally:  # Always executed if exceptions are caught or not
        print(num1, "/", num2, "=", result)


def validateAge(age):
    if age < 0:
        # throw intentionally an exception with custom message
        raise TypeError("negative ages are invalid")
    elif age < 20:
        print("You're too young")
    elif age < 40:
        print("You're young")
    elif age < 65:
        print("You're relatively young")
    else:
        print("Take care")


def main():
    validateAge(-20)
#   divideApp()

#    while True:
#       num1 = input("Digit number 1: ")
#       num2 = input("Digit number 2: ")
#       print(num1, "/", num2, "=", divide(num1, num2))


main()
