# fun with recursion
# CPE 551 B
# Spring 2023
# Kevin Ryan

def factorial(n):
  """assumes n>=0, returns n!"""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
  
print(factorial(5))

def mySum(L):
  """assume L is list of numbers, return sum(L)"""
  if L == []:
    return 0
  else:
    return L[0] + mySum(L[1:])
  
print(mySum([2,9,14]))