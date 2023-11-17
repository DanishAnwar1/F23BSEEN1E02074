def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Compare the string with its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Test the function with an example
example_number = 545
if is_palindrome(example_number):
    print(f"{example_number} is a palindrome number.")
else:
    print(f"{example_number} is not a palindrome number.")
