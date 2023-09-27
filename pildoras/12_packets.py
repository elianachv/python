"""
Class 35: Packages
Class 36: Distributable packages
Author: Eliana Chavez
"""

# Packages is a folder to group modules related
# Create a folder with a file named __init__.py
# It is possible to create subpackagess to organize better your code
# Each subpackages must have the file __init__.py
# Importing functions from modules in opackagess and subpackagess
from packet_example.basics.module_simple_calcs import substract
from packet_example.basics.module_simple_calcs import multiply
from packet_example.advanced.module_advanced_calcs import power


def main():
    print("Using functions from modules in subpackagess")
    print("2 ^ 2 = ", power(2, 2))
    print("2 * 2 = ", multiply(2, 2))


main()

# packagess could be distributable and they may be installed and used
# So it does not matter where in the code I call functions of a module
# Create setup.py file in the root . This file describes which packagess will be distributed
# Open terminal whre the setup.py file is and excute python setup.py sdist
# 2 folder will be created (dist with a zip folder and also module_name.egg-info)
# Install the compressed folder:
# Access dist folder in a terminal and execute pip3 install module_name
# Then any function of the packages will work even if the file is not in the same folder that the package
# NOTE: To uninstall the package execute pip3 uninstall module_name

def testDistributablePackages():
    print("2 - 2 = ", substract(2, 2))


testDistributablePackages()
