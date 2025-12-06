# WRITE A PROGRAM TO CREATE, CONCATENATE AND PRINT A STRING AND ACCESSING SUB-STRING FROM A GIVEN STRING.
# Taking string input from user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Concatenating the strings
combined_string = string1 + string2
print("Concatenated String:", combined_string)

# Accessing sub-strings
print("Substring from index 0 to 3:", combined_string[0:4])
print("Substring from index 2 to end:", combined_string[2:])
print("Last 3 characters:", combined_string[-3:])
