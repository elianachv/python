"""
Class 76: Docs and testing part 1
Class 77: Docs and testing part 2
Author: Eliana Chavez
"""

import doctest
import math

# doctest help us to implement some testing cases within the documentation
# We use >>> function() to specify the example
def add(num1: int, num2: int) -> int:
    """
    Add 2 numbers

    Params:
     num1: number 1 to add
     num2: number 2 to add

    Returns: 
      Add result

    >>> add(1, 1)
    2

    >>> add(2, 1)
    3

    >>> add(0, 1)
    1

    """
    return num1 + num2


def validateEmail(email: str) -> bool:
    """
    Validates if an email is correct, it must have one @ 
    and a valid termination (allowed: .com, .es, .co, .net)

    Params:
    email: emai to validate

    Returns:
    True if email is correct
    False if email is not valid

    >>> validateEmail("test@gmail.com")
    True

    >>> validateEmail("testerror")
    False
    """

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


def sqr(numbers: list) -> list:
    """
    Params:
    numbers: list of numbers

    Returns
    List with square root of each number in the list

    >>> numbers=[]
    >>> for i in [4, 9, 16]: 
    ...   numbers.append(i)
    >>> sqr(numbers)
    [2.0, 3.0, 4.0]


    >>> for i in [4, -9, 16]: 
    ...   numbers.append(i)
    >>> sqr(numbers)
    Traceback (most recent call last):
      ...
    ValueError: math domain error
    
    """

    return list(map(math.sqrt, numbers))
    # return [math.sqrt(n) for n in numbers]


def main():
    numbers = [9, 16, 25, 36]
    result = sqr(numbers)
    print("Numbers: ", numbers)
    print("Result: ", result)


# Activate docs tests
doctest.testmod()

# If we run the program and nothin appears it means everything is ok all tests have passed
