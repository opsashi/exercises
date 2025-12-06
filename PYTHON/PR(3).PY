# CONDITIONAL STATEMENT
# (I)IF STATEMENT
age =18
if age >= 18:
    print("you are an adult.")
# (ii)if else statement
num=5
if num>0:
    print("positive number")
else:
    print("non-positive number")
# (iii)if elif else statement
num=0
if num>0:
    print("positive")
elif num==0:
    print("zero")
else:
    print("negative")
# (iv)nested if statement
num=10
if num>0:
    print("number is postive")
    if num%2==0:
        print("positive even number")
    else:
        print("positive odd number")
else:
    print("not a positive number")