import random

# Create a random size matrix
max_x = random.randint(5, 10)  # Random height
max_y = random.randint(5, 10)  # Random width
matrix = [[' ' for _ in range(max_y)] for _ in range(max_x)]

# Draw the letter F
for i in range(max_x):
    matrix[i][0] = '*'  # Vertical line
for j in range(max_y // 2):
    matrix[0][j] = '*'  # Top horizontal line
for j in range(max_y // 2):
    matrix[max_x // 2][j] = '*'  # Middle horizontal line

# Print the matrix
for row in matrix:
    print(''.join(row))
