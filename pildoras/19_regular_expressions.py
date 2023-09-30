"""
Class 69: Regular expressions part 1: basics
Class 70: Regular expressions part 2: meta characters
Class 71: Regular expressions part 3
Class 72: Regular expressions part 4

Author: Eliana Chavez
"""


# Regular expressions are char secuences that form a search pattern
# NOTE: Regex does distinctions between upper and lower case

import re

chain = "Learning regex"
result = re.search("Learning", chain)

print("First char index:", result.start())
print("Last char index", result.end())
print("Show indexes:", result.span())
print("All matches: ", re.findall("regex", chain))

names = ["Ana Gomez", "Maria Martin", "Sandra Lopez", "Santiago Martin"]

print("\nStart (^)")
for name in names:
    if re.findall("^S", name):
        print(name, "starts with S")

print("\nEnd ($)")
for name in names:
    if re.findall("Martin$", name):
        print(name, "finish with Martin")


print("\nVariable values []")
for name in names:
    if re.findall("[zsS]", name):
        print(name, "contains z or s")


print("\nRange []")
for name in names:
    if re.findall("[o-t]", name):
        print(name, "contains o p q r s or t")


print("\nRange negative []")
for name in names:
    if re.findall("[^i]", name):
        print(name, " does not contain  i")


print("\nMatch")
for name in names:
    if re.match("Sandra", name, re.IGNORECASE):
        print(name, " is Sandra")
