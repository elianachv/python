"""
Class 73: Decorators part 1: Syntax and basic example
Class 74: Decorators part 2: Decorate function with params and advance example
Author: Eliana Chavez
"""

# Decorators add functionalities to a function
# Decorator returns a function

"""
Syntax:
def decorator(function):
  def internFunction():
    code ...
  return internFunction
"""

# Decorator example
def calcDecorator(calcFunction):
    def newFuncitonality():
        print("Initializing calc ...")
        calcFunction()
        print("Calc finished succesfully")
    return newFuncitonality

# Decorator that interacts with args 
# kwargs = Arguments key value
def calcDecorator_v2(calcFunction):
    def newFuncitonality(*args, **kwargs):
        print("Initializing calc ...")
        calcFunction(*args, **kwargs)
        print("Calc finished succesfully")
    return newFuncitonality

# Applying decorator
@calcDecorator
def add():
    print(1+1)


def substract():
    print(1-1)

# _________________________


@calcDecorator_v2
def add_v2(num1, num2):
    print(num1+num2)


def substract_v2(num1, num2):
    print(num1-num2)

@calcDecorator_v2
def pow(base, exponent):
    print(base**exponent)

def main():
    print("\nAdd function (decorated)")
    add()

    print("\nSubstract function")
    substract()

    print("\nAdd function with params (decorated)")
    add_v2(2, 2)

    print("\nPow function with params (decorated)")
    # Key value arguments (kwargs)
    pow(base=2, exponent=2)


main()
