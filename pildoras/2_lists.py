"""
Class 7: Lists
Author: Eliana Chavez
"""

# Lists
numbers = [1, 2, 3, 4, 5, 6, 7]
names = ["Eli", "Clementina", "Victoria", "Claudio", "Octavia", "Cornelio"]
mix = ["Text", 90, True]

# [1, 2, 3, 4, 5, 6, 7] ['Eli', 'Clementina', 'Victoria', 'Claudio', 'Octavia', 'Cornelio'] ['Text', 90, True]
print(numbers, names, mix)

# Victoria
print(names[2])

# Octavia
print(names[-2])

# [1,2,3]
print(numbers[0:3])
print(numbers[:3])

# [5, 6, 7]
print(numbers[4:])

# Add elements
mix.append("new")

# ['Text', 90, True, 'new']
print(mix)

mix.insert(1, "new in index 1")

# ['Text', 'new in index 1', 90, True, 'new']
print(mix)

# Add a list to anothe list
mix.extend([1, 2, 3])

# ['Text', 'new in index 1', 90, True, 'new', 1, 2, 3]
print(mix)

# Get the first index of an element

# 4
print(names.index("Octavia"))

# Exception: print(names.index("Helen"))

# Get if an element exists
print("Helen" in names)  # False
print("Cornelio" in names)  # True


# Remove an element
names.remove("Clementina");

# ['Eli', 'Victoria', 'Claudio', 'Octavia', 'Cornelio']
print(names)

# Remove the last element
names.pop()

# ['Eli', 'Victoria', 'Claudio', 'Octavia']
print(names)

# Adding lists
nn=numbers+names;

# [1, 2, 3, 4, 5, 6, 7, 'Eli', 'Victoria', 'Claudio', 'Octavia']
print(nn)

# Repeat lists

# ['Eli', 'Victoria', 'Claudio', 'Octavia', 'Eli', 'Victoria', 'Claudio', 'Octavia', 'Eli', 'Victoria', 'Claudio', 'Octavia']
print(names*3)