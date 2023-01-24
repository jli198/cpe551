# factorial.py
#   This program will calculate
#   factorial of a number entered
#   by the user

n = int(input("Please enter an integer: "))
fact = 1 # Initial condition!
for i in range(n,0,-1):
  fact = fact * i
print("The factorial of", n, "is", fact)