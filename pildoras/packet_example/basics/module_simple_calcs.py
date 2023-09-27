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

def power(num1,num2):
    if isinstance(num1, int) == False:
        num1 = int(num1)

    if isinstance(num2, int) == False:
        num2 = int(num2)
    
    return num1**num2