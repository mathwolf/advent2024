import numpy as np

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

# store word search as an array of ASCII codes
rows = len(lines)
cols = len(lines[0])
search_grid = np.ndarray((rows, cols), dtype=int)
for i, L in enumerate(lines):
    for j, c in enumerate(L):
        search_grid[i,j] = ord(c)

total = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if search_grid[i,j] == ord('A'):
            if (search_grid[i-1,j-1] == ord('M') and search_grid[i+1,j+1] == ord('S')) \
                or (search_grid[i-1,j-1] == ord('S') and search_grid[i+1,j+1] == ord('M')):            
                if (search_grid[i-1,j+1] == ord('M') and search_grid[i+1,j-1] == ord('S')) \
                    or (search_grid[i-1,j+1] == ord('S') and search_grid[i+1,j-1] == ord('M')):
                    total += 1
print(total)
