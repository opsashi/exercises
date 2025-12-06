# WRITE A PYTHON SCRIPT THAT PRINTS PRIME NUMBERS LESS THAN 20.
print("Prime numbers less than 20:")

for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
