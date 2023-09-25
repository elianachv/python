"""
Class 31: Inheritance, super and isinstance example
Author: Eliana Chavez
"""

class Person():
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def description(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nLocation: " + self.location


class Employee(Person):
    def __init__(self, name, age, location, salary, company):
        # super() calls init method of parent class
        super().__init__(name, age, location)
        self.salary = salary
        self.company = company

    def description(self):
        return super().description() + "\nCompany: " + self.company + "\nSalary: " + str(self.salary)


def superExample():
    antonio = Employee("Antonio", 34, "Bogota", 10000, "Google")
    print(antonio.description())

    print(antonio.name, " is a person? ", isinstance(antonio, Person))
    print(antonio.name, " is an employee? ", isinstance(antonio, Employee))


def main():
    superExample()


main()
