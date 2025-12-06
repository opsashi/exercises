# WRITE A PROGRAM TO PRINT THE SUM OF ALL THE EVEN NUMBERS IN THE RANGE 1-50 
# Initialize sum
even_sum = 0

# Loop through numbers from 1 to 50
for i in range(1, 50):
    if i % 2 == 0:
        even_sum += i

# Print the result
print("Sum of even numbers from 1 to 50 is:", even_sum)
