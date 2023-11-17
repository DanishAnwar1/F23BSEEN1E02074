def check_first_last_equal(numbers):
    # Check if the list is not empty
    if len(numbers) >= 2:
        # Compare the first and last elements
        return numbers[0] == numbers[-1]
    else:
        # If the list has less than two elements, they cannot be the same
        return False

# Given lists
number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35.75, 30]

# Check for number_x
result_x = check_first_last_equal(number_x)
if result_x:
    print("For number_x:",True)
else:
    print("For number_x:",False)

# Check for number_y
result_y = check_first_last_equal(number_y)
if result_y:
    print("For number_y:",True)
else:
    print("For number_y:",False)
