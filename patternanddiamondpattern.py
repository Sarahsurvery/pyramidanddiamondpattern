# Python program to draw a pyramid of '*'

# Get the number of rows for the pyramid from the user
rows = int(input("Enter the number of rows for the pyramid: "))

# Loop to print the pyramid
for i in range(1, rows + 1):
    spaces = " " * (rows - i)  # Create leading spaces
    stars = "*" * (2 * i - 1)  # Create the star pattern
    print(spaces + stars)  # Print the centered pyramid row

# Python program to draw a diamond of '*'

# Get the number of rows for the upper half from the user
rows = int(input("Enter the number of rows for the diamond (half part): "))

# Loop to print the upper pyramid
for i in range(1, rows + 1):
    spaces = " " * (rows - i)  # Create leading spaces
    stars = "*" * (2 * i - 1)  # Create the star pattern
    print(spaces + stars)  # Print the centered pyramid row

# Loop to print the inverted pyramid (lower half)
for i in range(rows - 1, 0, -1):
    spaces = " " * (rows - i)  # Create leading spaces
    stars = "*" * (2 * i - 1)  # Create the star pattern
    print(spaces + stars)  # Print the centered pyramid row


