# Exercise 2: Print the sum of the current number and the previous number.
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current
# and previous number


for i in range(1, 11):
    current_number = i
    previous_number = i - 1 if i > 0 else 0
    sum_of_numbers = current_number + previous_number
    print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum_of_numbers}")
