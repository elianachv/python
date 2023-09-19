"""
Class 9: Diccionaries
Author: Eliana Chavez
"""

countries = {"Colombia": "Bogota", "German": "Berlin",
             "France": "Paris", "Argentina": "Buenos Aires"}

# {'Colombia': 'Bogota', 'German': 'Berlin', 'France': 'Paris', 'Argentina': 'Buenos Aires'}
print(countries)

# Bogota
print(countries.get("Colombia"))
print(countries["Colombia"])

# Add new element
countries["Italy"] = "Pekin"

# Pekin
print(countries["Italy"])

# Update a value
countries["Italy"] = "Rome"

# Rome
print(countries["Italy"])

# Delete element
del countries["France"]

# {'Colombia': 'Bogota', 'German': 'Berlin', 'Argentina': 'Buenos Aires', 'Italy': 'Rome'}
print(countries)

mix = {23: "Jordan", "Songs": 5, 12: 70}

# {23: 'Jordan', 'Songs': 5, 12: 70}
print(mix)
print(mix)

# Assign tuples values to diccionary
countriesTuple = ("Spain", "Peru", "USA")

countriesDiccionary = {countriesTuple[0]: "Madrid",
                       countriesTuple[1]: "Lima", 
                       countriesTuple[2]: "Washinton D.C"}

# {'Spain': 'Madrid', 'Peru': 'Lima', 'USA': 'Washinton D.C'}
print(countriesDiccionary)

# Diccionary in diccionary
countries["Extras"]=countriesDiccionary;

# {'Colombia': 'Bogota', 'German': 'Berlin', 'Argentina': 'Buenos Aires', 'Italy': 'Rome', 'Extras': {'Spain': 'Madrid', 'Peru': 'Lima', 'USA': 'Washinton D.C'}}
print(countries)

# dict_keys(['Colombia', 'German', 'Argentina', 'Italy', 'Extras'])
print(countries.keys())

# dict_values(['Bogota', 'Berlin', 'Buenos Aires', 'Rome', {'Spain': 'Madrid', 'Peru': 'Lima', 'USA': 'Washinton D.C'}])
print(countries.values())

# 5
print(len(countries))