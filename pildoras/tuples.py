"""
Class 8: Tuples
Author: Eliana Chavez
"""

# Tuples are more restrictive than lists but they're faster and lighter than lists

names = ("Victoria", "Clementina", "Claudio")
numbers = (1, 2, 3, 4)

# 3
print(numbers[2])

# Convert tuple in list
namesLists = list(names)

# ("Victoria","Clementina","Claudio")
print(names)
# ["Victoria","Clementina","Claudio"]
print(namesLists)

# Convert list in tuple
namesTuple = tuple(namesLists)

# ("Victoria","Clementina","Claudio")
print(namesTuple)

# False
print("Wilson" in names)

# 1
print(names.count("Clementina"))

# 3
print(len(namesTuple))

unitaryTuple=("Test",)

# 1
print(len(unitaryTuple))
print(unitaryTuple)

# Unpacking tuple
info=("Eli",17,4,2000)
name, day, month, year = info;

print("Name:", name)
print("Day:", day)
print("Month:", month)
print("Year:", year)