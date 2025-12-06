# WRITE A PROGRAM TO SWAP TWO NUMBERS WITHOUT USING A TEMOPARARY VARIABLE.
# Input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Swapping without using a temporary variable
a = a + b
b = a - b
a = a - b

# Result after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
