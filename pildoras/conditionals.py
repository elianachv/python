"""
Class 10: Conditionals part 1
Author: Eliana Chavez
"""

def quiz(score):
  status="none"
  if score>7:
    status="approved"
  else:
    status= "failed"
  return status


print(quiz(3))
print(quiz(8))