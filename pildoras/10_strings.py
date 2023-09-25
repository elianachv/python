"""
Class 33: Strings methods
Author: Eliana Chavez
"""

"""
upper(): aaa -> AAA
lower(): AAA -> aaa
capitalize(): aaa -> Aaa
count(): aaa -> 3
isdigit(): aaa -> False - 43 -> True
isalum(): aaa -> False - a45 -> True - 45 -> False
isalpha(): aaa -> True
split(): "a a a".split(" ") -> ["a","a","a"]
strip(): "a a a".strip() -> "aaa"
replace(): aaa.replace(a,e) -> eee
find(): aaa -> 0

More info: https://www.w3schools.com/python/python_ref_string.asp
"""


def main():
    user = input("Introduce your username: ")

    print("Natural: ", user)
    print("Lower: ", user.lower())
    print("Upper: ", user.upper())
    print("Capitalize: ", user.capitalize())

    age = input("Introduce your age: ")
    print("Correct age: ", age.isdigit())


main()
