# WRITE A PROGRAM TO DEMONSTRATE DIFFERENT NUMBER DATA TYPES IN PYTHON (I.E.,INT,FLOAT,COMPLEX,BOOL AND STRING TYPES).

# Input as integer
a = int(input("Enter an integer (e.g., 2): "))
print("Integer:", a, "Type:", type(a))

# Input as float
b = float(input("Enter a float number (e.g., 2.0): "))
print("Float:", b, "Type:", type(b))

# Input as complex number
c = complex(input("Enter a complex number (e.g., 2+3j): "))
print("Complex:", c, "Type:", type(c))

# Input as boolean
d = input("Enter True or False (Boolean): ")  # This will be string
d = d == "True"  # Convert to Boolean
print("Boolean:", d, "Type:", type(d))

# Input as string
e = input("Enter a string (e.g., Name): ")
print("String:", e, "Type:", type(e))
