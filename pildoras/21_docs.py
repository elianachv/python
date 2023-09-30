"""
Class 75: Documenting you programs
Author: Eliana Chavez
"""
from modules import module_example

class Calcs:
  """
  This class meake some area calcs
  """
    
  def calcTriangleArea(base: float, height: float):
      """
      This is a documentation example:
      Calcs area of a triangle
      """
      return (base*height)/2


  def calcSquareArea(side: float):
      """
      This is a documentation example:
      Calcs area of a square
      """
      return side*side

def main():
    print("Executing functions")
    print(Calcs.calcTriangleArea(4, 7))
    print(Calcs.calcSquareArea(4))

    print("Printing functions' docs:")
    print(Calcs.calcTriangleArea.__doc__)
    print(Calcs.calcSquareArea.__doc__)

    print("Accessing functions' docs through help command")
    help(Calcs.calcTriangleArea)
    help(Calcs.calcSquareArea)

    print("Class docs")
    help(Calcs)

    print("Printing module docs")
    help(module_example)
 

main()