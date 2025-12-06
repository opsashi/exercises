# WRITE A PROGRAM TO DISPLAY ALL PRIME NUMBERS WITHIN AN INTERVAL OF 20 AND 50
print("Prime numbers between 20 and 50:")

for num in range(20, 50):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
