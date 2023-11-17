# Exercise 3: Print characters from a string that are present at an even index number.

# Write a program to accept a string from the user and display characters that are  present at an even index number.

# Accept the string from user
user_input=input("Entre the string:") 
# Display characters at even index numbers
even_index_number=user_input[::2]
print(f"even_index_characters:{even_index_number}")