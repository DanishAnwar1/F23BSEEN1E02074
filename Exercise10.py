# Print multiplication table from 1 to 10
for i in range(1, 11):  # Outer loop for the multiplicand
    print(f"\nMultiplication table for {i}:")
    for j in range(1, 11):  # Inner loop for the multiplier
        result = i * j
        print(f"{i} x {j} = {result}")
