# Given lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Initialize an empty list to store the result
new_list = []

# Iterate through the first list and add odd numbers to the new list
for number in list1:
    if number % 2 != 0:
        new_list.append(number)

# Iterate through the second list and add even numbers to the new list
for number in list2:
    if number % 2 == 0:
        new_list.append(number)

# Print the resulting list
print("New list:", new_list)
