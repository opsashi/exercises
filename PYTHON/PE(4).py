def countvowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for c in text:          # Loop through each character
        if c in vowels:     # Check if it’s a vowel
            count += 1      # Increase count if vowel
    return count            # Return total count after loop ends

# Take user input
text = input("Enter your text: ")
print("The count of vowels: ", countvowels(text))
