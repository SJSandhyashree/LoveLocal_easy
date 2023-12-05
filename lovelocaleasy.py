# Define a function named length_of_last_word that takes a string s as input
def length_of_last_word(s):
    # Split the string into a list of words using spaces as separators
    words = s.split()
    
    # Check if the list of words is not empty
    if words:
        # Return the length of the last word in the list
        return len(words[-1])
    else:
        # If the list is empty, return 0
        return 0

# Prompt the user to enter a string and store it in the variable user_input
user_input = input("Enter a string: ")

# Calculate the length of the last word in the user-inputted string
result = length_of_last_word(user_input)

# Display the result
print("Length of the last word:", result)