
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
            guard_start = (i, j, UP)

total = 0
for r in range(rows):
    for c in range(cols):
        if (r,c) in obstacles:
            continue

        obstacles.add((r,c))
        visited_states = {guard_start}
        guard = guard_start
        while True:
            if guard[2] == UP:
                if (guard[0] - 1, guard[1]) in obstacles:
                    guard = (guard[0], guard[1], RIGHT)
                else:
                    guard = (guard[0] - 1, guard[1], guard[2])
            elif guard[2] == RIGHT:
                if (guard[0], guard[1] + 1) in obstacles:
                    guard = (guard[0], guard[1], DOWN)
                else:
                    guard = (guard[0], guard[1] + 1, guard[2])
            elif guard[2] == DOWN:
                if (guard[0] + 1, guard[1]) in obstacles:
                    guard = (guard[0], guard[1], LEFT)
                else:
                    guard = (guard[0] + 1, guard[1], guard[2])
            else:
                if (guard[0], guard[1] - 1) in obstacles:
                    guard = (guard[0], guard[1], UP)
                else:
                    guard = (guard[0], guard[1] - 1, guard[2])

            if guard[0] < 0 or guard[0] >= rows or guard[1] < 0 \
                or guard[1] >= cols:
                obstacles.remove((r,c))
                break
            elif guard in visited_states:
                total += 1
                obstacles.remove((r,c))
                break
            else:
                visited_states.add(guard)
print(total)
