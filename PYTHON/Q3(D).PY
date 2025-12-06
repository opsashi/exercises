# WRITE A PYTHON PROGRAM TO FIND FACTORIAL OF A NUMBER USING RECURSION.
# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from user
num = int(input("Enter a number: "))

# Check for negative input
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")
