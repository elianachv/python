"""
Class 34: Modules
Use module
Author: Eliana Chavez
"""
# Importing the module it requires to specify
# the name of the module each time we want to use a funciton

# Module file must be in the same directory of the file tha uses it

# Importing examples:
# import module_example
# from module_example import add, substract

# Importing all using * is not the best practice
# 'cause it reserves a big space in memory
from module_example import *


def main():

    print("1 + 1 =", add(1, 1))
    print("1 - 1 =", substract(1, 1))
    print("1 * 1 =", multiply(1, 1))
    print("1 / 1 =", (divide(1, 1)))

main()
