import numpy as np

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

PATH = 0
ROCK = 1
rows = len(lines)
cols = len(lines[0])
maze = np.empty((rows, cols), dtype=int)
candidate_nodes = {}
for i, L in enumerate(lines):
    for j, c in enumerate(L):
        if c == 'S':
            maze[i,j] = PATH
            candidate_nodes[(i, j, RIGHT)] = 0
        elif c == 'E':
            maze[i,j] = PATH
            end_location = (i,j)
        elif c == '.':
            maze[i,j] = PATH
        else:
            maze[i,j] = ROCK

# Dijkstra's algorithm
processed_nodes = {}
while candidate_nodes:
    current_node = min(candidate_nodes, key = lambda z: candidate_nodes[z])
    # print(current_node)

    i = current_node[0]
    j = current_node[1]
    facing = current_node[2]
    cost = candidate_nodes[current_node]

    if (i,j) == end_location:
        print(cost)
        exit()

    if facing == UP:
        # move up if possible
        if maze[i-1,j] != ROCK and (i-1, j, UP) not in processed_nodes:
            new_cost = cost + 1
            if (i-1, j, UP) in candidate_nodes:
                candidate_nodes[(i-1, j, UP)] = \
                    min(new_cost, candidate_nodes[(i-1, j, UP)])
            else:
                candidate_nodes[(i-1, j, UP)] = new_cost
        # turn 90 right
        if (i, j, RIGHT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, RIGHT) in candidate_nodes:
                candidate_nodes[(i, j, RIGHT)] = \
                    min(new_cost, candidate_nodes[(i, j, RIGHT)])
            else:
                candidate_nodes[(i, j, RIGHT)] = new_cost
        # turn 90 left
        if (i, j, LEFT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, LEFT) in candidate_nodes:
                candidate_nodes[(i, j, LEFT)] = \
                    min(new_cost, candidate_nodes[(i, j, LEFT)])
            else:
                candidate_nodes[(i, j, LEFT)] = new_cost
        
    elif facing == RIGHT:
        # move right if possible
        if maze[i,j+1] != ROCK and (i, j+1, RIGHT) not in processed_nodes:
            new_cost = cost + 1
            if (i, j+1, RIGHT) in candidate_nodes:
                candidate_nodes[(i, j+1, RIGHT)] = \
                    min(new_cost, candidate_nodes[(i, j+1, RIGHT)])
            else:
                candidate_nodes[(i, j+1, RIGHT)] = new_cost
        # turn 90 right
        if (i, j, DOWN) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, DOWN) in candidate_nodes:
                candidate_nodes[(i, j, DOWN)] = \
                    min(new_cost, candidate_nodes[(i, j, DOWN)])
            else:
                candidate_nodes[(i, j, DOWN)] = new_cost
        # turn 90 left
        if (i, j, UP) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, UP) in candidate_nodes:
                candidate_nodes[(i, j, UP)] = \
                    min(new_cost, candidate_nodes[(i, j, UP)])
            else:
                candidate_nodes[(i, j, UP)] = new_cost
        
    elif facing == DOWN:
        # move down if possible
        if maze[i+1,j] != ROCK and (i+1, j, DOWN) not in processed_nodes:
            new_cost = cost + 1
            if (i+1, j, DOWN) in candidate_nodes:
                candidate_nodes[(i+1, j, DOWN)] = \
                    min(new_cost, candidate_nodes[(i+1, j, DOWN)])
            else:
                candidate_nodes[(i+1, j, DOWN)] = new_cost
        # turn 90 right
        if (i, j, LEFT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, LEFT) in candidate_nodes:
                candidate_nodes[(i, j, LEFT)] = \
                    min(new_cost, candidate_nodes[(i, j, LEFT)])
            else:
                candidate_nodes[(i, j, LEFT)] = new_cost
        # turn 90 left
        if (i, j, RIGHT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, RIGHT) in candidate_nodes:
                candidate_nodes[(i, j, RIGHT)] = \
                    min(new_cost, candidate_nodes[(i, j, RIGHT)])
            else:
                candidate_nodes[(i, j, RIGHT)] = new_cost
        
    else:   # facing LEFT
        # move left if possible
        if maze[i,j-1] != ROCK and (i, j-1, LEFT) not in processed_nodes:
            new_cost = cost + 1
            if (i, j-1, LEFT) in candidate_nodes:
                candidate_nodes[(i, j-1, LEFT)] = \
                    min(new_cost, candidate_nodes[(i, j-1, LEFT)])
            else:
                candidate_nodes[(i, j-1, LEFT)] = new_cost
        # turn 90 right
        if (i, j, UP) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, UP) in candidate_nodes:
                candidate_nodes[(i, j, UP)] = \
                    min(new_cost, candidate_nodes[(i, j, UP)])
            else:
                candidate_nodes[(i, j, UP)] = new_cost
        # turn 90 left
        if (i, j, DOWN) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, DOWN) in candidate_nodes:
                candidate_nodes[(i, j, DOWN)] = \
                    min(new_cost, candidate_nodes[(i, j, DOWN)])
            else:
                candidate_nodes[(i, j, DOWN)] = new_cost
        
    processed_nodes[current_node] = cost
    del candidate_nodes[current_node]

    # print(processed_nodes)
    # print(candidate_nodes)
