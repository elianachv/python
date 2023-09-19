"""
Class 5: Functions part 1
Class 6: Functions part 2
Author: Eliana Chavez
"""
# Predefined functions example: print
# Own functions example hello

def hello(): print("Hello World!")

def add(num1, num2):

    if isinstance(num1, int) == False:
        num1 = int(num1)

    if isinstance(num2, int) == False:
        num2 = int(num2)

    return num1 + num2

def substract(num1, num2):

    if isinstance(num1, int) == False:
        num1 = int(num1)

    if isinstance(num2, int) == False:
        num2 = int(num2)

    return num1 - num2

def multiply(num1, num2):

    if isinstance(num1, int) == False:
        num1 = int(num1)

    if isinstance(num2, int) == False:
        num2 = int(num2)

    return num1 * num2

def divide(num1, num2):

    if isinstance(num1, int) == False:
        num1 = int(num1)

    if isinstance(num2, int) == False:
        num2 = int(num2)

    if num2 == 0:
        return 0;

    return num1 / num2

def main():
    hello()
    num1 = input("Digit number 1: ")
    num2 = input("Digit number 2: ")
    print(num1,"+",num2,"=",add(num1, num2))
    print(num1,"-",num2,"=",substract(num1, num2))
    print(num1,"*",num2,"=",multiply(num1, num2))
    print(num1,"/",num2,"=",divide(num1, num2))

main()
