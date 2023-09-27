def power(num1, num2):
    if isinstance(num1, int) == False:
        num1 = int(num1)

    if isinstance(num2, int) == False:
        num2 = int(num2)

    return num1**num2
