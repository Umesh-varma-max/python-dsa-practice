n = int(input())  
size = 2 * n - 1  
for i in range(size):
    for j in range(size):
        min_dist = min(i, j, size - 1 - i, size - 1 - j)
        print(n - min_dist, end=" ")
    print()
'''
n = int(input())  
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        top = i
        left = j
        right = size - 1 - j
        bottom = size - 1 - i
        layer = min(top, bottom, left, right)
        
        print(n - layer, end=" ")
    print()
'''
'''
n = int(input())  # Example: n = 5
size = 2 * n - 1

matrix = [[0 for _ in range(size)] for _ in range(size)]

for layer in range(n):
    val = n - layer
    # Top and Bottom rows
    for i in range(layer, size - layer):
        matrix[layer][i] = val
        matrix[size - layer - 1][i] = val
    # Left and Right columns
    for i in range(layer, size - layer):
        matrix[i][layer] = val
        matrix[i][size - layer - 1] = val

# Print the matrix
for row in matrix:
    print(" ".join(str(x) for x in row))
'''