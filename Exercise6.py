def downward_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=' ')
        print()

# Example: To print a downward half-pyramid with 5 rows
downward_half_pyramid(5)
