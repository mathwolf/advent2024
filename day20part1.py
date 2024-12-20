import numpy as np

# for debugging
def display_grid():
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == WALL:
                print('##', end='')
            elif (r,c) in path:
                if 0<= grid[r,c] <= 9:
                    print(' ' + str(grid[r,c]), end='')
                else:
                    print(grid[r,c], end='')
            else:
                print('..', end='')
        print('')
    print('')


with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

WALL = -1
PATH = 0
rows = len(lines)
cols = len(lines[0])
grid = np.empty((rows, cols), dtype=int)
for i, L in enumerate(lines):
    for j, c in enumerate(L):
        if c == '#':
            grid[i,j] = WALL
        elif c == 'S':
            grid[i,j] = PATH
            start = (i,j)
        elif c == 'E':
            grid[i,j] = PATH
            end = (i,j)
        else:
            grid[i,j] = PATH

# generate the default path through the grid
path = []
current_cell = start
path.append(start)
grid[current_cell] = 0
while current_cell != end:
    r = current_cell[0]
    c = current_cell[1]

    if c - 1 >= 0 and grid[r, c-1] == PATH \
        and (r, c-1) not in path:
        path.append((r, c-1))        
    elif c + 1 < cols and grid[r, c+1] == PATH \
        and (r, c+1) not in path:
        path.append((r, c+1))        
    elif r - 1 >= 0 and grid[r-1, c] == PATH \
        and (r-1, c) not in path:
        path.append((r-1, c))        
    else:
        path.append((r+1, c))
    current_cell = path[-1]
    grid[current_cell] = len(path) - 1

# calculate length for cheats
cheats = {}
for p in path:
    r = p[0]
    c = p[1]
    if c - 2 >= 0 and grid[r, c-1] == WALL \
        and grid[r, c-2] > grid[r,c]:
        cheats[(r, c, r, c-2)] = grid[r, c-2] - grid[r, c] - 2
    if c + 2 < cols and grid[r, c+1] == WALL \
        and grid[r, c+2] > grid[r,c]:
        cheats[(r, c, r, c+2)] = grid[r, c+2] - grid[r, c] - 2
    if r - 2 >= 0 and grid[r-1, c] == WALL \
        and grid[r-2, c] > grid[r,c]:
        cheats[(r, c, r-2, c)] = grid[r-2, c] - grid[r, c] - 2
    if r + 2 < rows and grid[r+1, c] == WALL \
        and grid[r+2, c] > grid[r,c]:
        cheats[(r, c, r+2, c)] = grid[r+2, c] - grid[r, c] - 2


total = 0
for c in cheats.keys():
    if cheats[c] >= 100:
        total += 1
print(total)
