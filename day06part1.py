
with open('input.txt', 'r') as f:
    input_grid = f.read().split('\n')

UP, LEFT, DOWN, RIGHT = 1, 2, 3, 4
rows = len(input_grid)
cols = len(input_grid[0])
obstacles = set()
for i, r in enumerate(input_grid):
    for j, c in enumerate(r):
        if c == '#':
            obstacles.add((i,j))
        elif c == '^':
            guard = (i,j)
            facing = UP

visited_cells = {guard}
while True:
    if facing == UP:
        if (guard[0] - 1, guard[1]) in obstacles:
            facing = RIGHT
            continue
        else:
            guard = (guard[0] - 1, guard[1])
    elif facing == RIGHT:
        if (guard[0], guard[1] + 1) in obstacles:
            facing = DOWN
            continue
        else:
            guard = (guard[0], guard[1] + 1)
    elif facing == DOWN:
        if (guard[0] + 1, guard[1]) in obstacles:
            facing = LEFT
            continue
        else:
            guard = (guard[0] + 1, guard[1])
    else:
        if (guard[0], guard[1] - 1) in obstacles:
            facing = UP
            continue
        else:
            guard = (guard[0], guard[1] - 1)

    if guard[0] < 0 or guard[0] >= rows or guard[1] < 0 \
        or guard[1] >= cols:
        break
    visited_cells.add(guard)
print(len(visited_cells))
