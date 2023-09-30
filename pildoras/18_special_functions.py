"""
Class 66: Lambda functions
Class 67: Filter function
Class 68: Map function
Author: Eliana Chavez
"""

# traditional function
def calcTriangleArea(base, height):
    return (base*height)/2


# lambda function
triangleArea = lambda base, height: (base*height)/2

# Lambda function is useful for short functions
# lambda functions are also called on the go, on demand or online functions
def lambdaFunctionExample():
    print("\nLambda functions example")
    print("Triangle area (traditional function):", calcTriangleArea(5, 7))
    print("Triangle area (lambda function):", triangleArea(5, 7))

# ______________________________________


def evenNumber(num):
    return num % 2 == 0


def filterFunctionExample():
    print("\nFilter functions example: Filter even numbers")
    numbers = [2, 15, 18, 20, 66, 54, 58, 57, 33]
    print(list(filter(evenNumber, numbers)))


# Filter functions is usually used to filter objects
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} has a salary of {}".format(self.name, self.salary)


def filterFunctionExample2():
    print("\nFilter functions example: Filter employees with salary > 1000")
    employees = [
        Employee("Ana", 1500), 
        Employee("Mark", 1000), 
        Employee("Sara", 2000)]
    
    filteredEmployees = filter(
        lambda employee: employee.salary > 1000, employees)
   
    for e in filteredEmployees:
        print(e.__str__())


# ______________________________________
# Map function apply a funtion to each element of iterable (list, tuples, etc) it returns  a list with the results

def applyCommission(employee):
    
    if employee.salary <= 1500:
      employee.salary *= 1.03
    return employee

def mapFunctionExample():
    print("\nMap functions example: calc salary with commissions")
    employees = [
        Employee("Ana", 1500), 
        Employee("Mark", 1000), 
        Employee("Sara", 2000)]
    
    employeesCommission = map(applyCommission, employees)
   
    for e in employeesCommission:
        print(e.__str__())
    

def main():
    lambdaFunctionExample()
    filterFunctionExample()
    filterFunctionExample2()
    mapFunctionExample()


main()
