import re
import numpy as np

# WIDTH = 11
# HEIGHT = 7
WIDTH = 101
HEIGHT = 103

class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __str__(self):
        return_str = 'p=' + str(self.x) + ',' + str(self.y) \
            + ' v=' + str(self.dx) + ',' + str(self.dy)
        return return_str
    
    def update(self):
        self.x = (self.x + self.dx) % WIDTH
        self.y = (self.y + self.dy) % HEIGHT

# for debugging purposes
def display_grid():
    grid = np.zeros((HEIGHT, WIDTH), dtype=int)

    for r in robots:
        grid[r.y, r.x] += 1
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(grid[i,j], end=' ')
        print('')


with open('input.txt', 'r') as f:
    input_lines = f.read().split('\n')

robots = set()
for L in input_lines:
    x, y, dx, dy = map(int, re.findall(r'-?\d+', L))
    robots.add(Robot(x, y, dx, dy))

total_time = 100
for t in range(total_time):
    for r in robots:
        r.update()


grid = np.zeros((HEIGHT, WIDTH), dtype=int)
for r in robots:
    grid[r.y, r.x] += 1

# count robots by quadrant
safety_factor = 1

total_robots = 0
for i in range(HEIGHT // 2):
    for j in range(WIDTH // 2):
        total_robots += grid[i,j]
safety_factor *= total_robots

total_robots = 0
for i in range(HEIGHT // 2 + 1, HEIGHT):
    for j in range(WIDTH // 2):
        total_robots += grid[i,j]
safety_factor *= total_robots

total_robots = 0
for i in range(HEIGHT // 2):
    for j in range(WIDTH // 2 + 1, WIDTH):
        total_robots += grid[i,j]
safety_factor *= total_robots

total_robots = 0
for i in range(HEIGHT // 2 + 1, HEIGHT):
    for j in range(WIDTH // 2 + 1, WIDTH):
        total_robots += grid[i,j]
safety_factor *= total_robots

print(safety_factor)

