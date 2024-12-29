import numpy as np

# idea: while processing each node, we keep track of the number of valid paths that
# brought us to that state

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

class Node:
    def __init__(self, cost, paths, path_list):
        self.cost = cost
        self.paths = paths
        self.path_list = path_list
        # list of list of tuples
        # each sublist is one distinct, optimal path to reach current position

    def __str__(self):
        return_str = 'cost: ' + str(self.cost) + '\n'
        return_str += 'paths: ' + str(self.paths) + '\n'
        for p in self.path_list:
            return_str += '{' 
            for n in p:
                return_str += '(' + str(n[0]) + ',' + str(n[1]) + ',' + str(n[2]) + ')'
            return_str += '}\n'
        return return_str
    

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
            candidate_nodes[(i, j, RIGHT)] = Node(0, 1, [[(i,j, RIGHT)]])
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
    current_node = min(candidate_nodes, key = lambda z: candidate_nodes[z].cost)
    # print(current_node)
    # exit()

    i = current_node[0]
    j = current_node[1]
    facing = current_node[2]
    cost = candidate_nodes[current_node].cost
    paths = candidate_nodes[current_node].paths
    path_list = candidate_nodes[current_node].path_list

    if (i,j) == end_location:
        print(cost)
        print(paths)
        optimal_seats = set()
        for p in path_list:
            for n in p:
                optimal_seats.add((n[0], n[1]))
        print(len(optimal_seats))
        exit()

    if facing == UP:
        # move up if possible
        if maze[i-1,j] != ROCK and (i-1, j, UP) not in processed_nodes:
            new_cost = cost + 1
            if (i-1, j, UP) in candidate_nodes:
                # by default, we expect the new cost to be greater than the
                # previous cost, in which case we do nothing - otherwise:
                if new_cost == candidate_nodes[(i-1, j, UP)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i-1, j, UP))
                        candidate_nodes[(i-1, j, UP)].path_list.append(np)
                    candidate_nodes[(i-1, j, UP)].paths += paths
            else:
                # add next step to end of all paths on the list
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i-1, j, UP))
                    new_path_list.append(np)
                candidate_nodes[(i-1, j, UP)] = Node(new_cost, paths, new_path_list)
        # turn 90 right
        if (i, j, RIGHT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, RIGHT) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, RIGHT)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, RIGHT))
                        candidate_nodes[(i, j, RIGHT)].path_list.append(np)
                    candidate_nodes[(i, j, RIGHT)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, RIGHT))
                    new_path_list.append(np)
                candidate_nodes[(i, j, RIGHT)] = Node(new_cost, paths, new_path_list)
        # turn 90 left
        if (i, j, LEFT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, LEFT) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, LEFT)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, LEFT))
                        candidate_nodes[(i, j, LEFT)].path_list.append(np)
                    candidate_nodes[(i, j, LEFT)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, LEFT))
                    new_path_list.append(np)
                candidate_nodes[(i, j, LEFT)] = Node(new_cost, paths, new_path_list)
        
    elif facing == RIGHT:
        # move right if possible
        if maze[i,j+1] != ROCK and (i, j+1, RIGHT) not in processed_nodes:
            new_cost = cost + 1
            if (i, j+1, RIGHT) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j+1, RIGHT)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j+1, RIGHT))
                        candidate_nodes[(i, j+1, RIGHT)].path_list.append(np)
                    candidate_nodes[(i, j+1, RIGHT)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j+1, RIGHT))
                    new_path_list.append(np)
                candidate_nodes[(i, j+1, RIGHT)] = Node(new_cost, paths, new_path_list)
        # turn 90 right
        if (i, j, DOWN) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, DOWN) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, DOWN)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, DOWN))
                        candidate_nodes[(i, j, DOWN)].path_list.append(np)
                    candidate_nodes[(i, j, DOWN)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, DOWN))
                    new_path_list.append(np)
                candidate_nodes[(i, j, DOWN)] = Node(new_cost, paths, new_path_list)
        # turn 90 left
        if (i, j, UP) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, UP) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, UP)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, UP))
                        candidate_nodes[(i, j, UP)].path_list.append(np)
                    candidate_nodes[(i, j, UP)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, UP))
                    new_path_list.append(np)
                candidate_nodes[(i, j, UP)] = Node(new_cost, paths, new_path_list)
        
    elif facing == DOWN:
        # move down if possible
        if maze[i+1,j] != ROCK and (i+1, j, DOWN) not in processed_nodes:
            new_cost = cost + 1
            if (i+1, j, DOWN) in candidate_nodes:
                if new_cost == candidate_nodes[(i+1, j, DOWN)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i+1, j, DOWN))
                        candidate_nodes[(i+1, j, DOWN)].path_list.append(np)
                    candidate_nodes[(i+1, j, DOWN)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i+1, j, DOWN))
                    new_path_list.append(np)
                candidate_nodes[(i+1, j, DOWN)] = Node(new_cost, paths, new_path_list)
        # turn 90 right
        if (i, j, LEFT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, LEFT) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, LEFT)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, LEFT))
                        candidate_nodes[(i, j, LEFT)].path_list.append(np)
                    candidate_nodes[(i, j, LEFT)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, LEFT))
                    new_path_list.append(np)
                candidate_nodes[(i, j, LEFT)] = Node(new_cost, paths, new_path_list)
        # turn 90 left
        if (i, j, RIGHT) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, RIGHT) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, RIGHT)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, RIGHT))
                        candidate_nodes[(i, j, RIGHT)].path_list.append(np)
                    candidate_nodes[(i, j, RIGHT)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, RIGHT))
                    new_path_list.append(np)
                candidate_nodes[(i, j, RIGHT)] = Node(new_cost, paths, new_path_list)
        
    else:   # facing LEFT
        # move left if possible
        if maze[i,j-1] != ROCK and (i, j-1, LEFT) not in processed_nodes:
            new_cost = cost + 1
            if (i, j-1, LEFT) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j-1, LEFT)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j-1, LEFT))
                        candidate_nodes[(i, j-1, LEFT)].path_list.append(np)
                    candidate_nodes[(i, j-1, LEFT)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j-1, LEFT))
                    new_path_list.append(np)
                candidate_nodes[(i, j-1, LEFT)] = Node(new_cost, paths, new_path_list)
        # turn 90 right
        if (i, j, UP) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, UP) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, UP)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, UP))
                        candidate_nodes[(i, j, UP)].path_list.append(np)
                    candidate_nodes[(i, j, UP)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, UP))
                    new_path_list.append(np)
                candidate_nodes[(i, j, UP)] = Node(new_cost, paths, new_path_list)
        # turn 90 left
        if (i, j, DOWN) not in processed_nodes:
            new_cost = cost + 1000
            if (i, j, DOWN) in candidate_nodes:
                if new_cost == candidate_nodes[(i, j, DOWN)].cost:
                    for p in path_list:
                        np = p.copy()
                        np.append((i, j, DOWN))
                        candidate_nodes[(i, j, DOWN)].path_list.append(np)
                    candidate_nodes[(i, j, DOWN)].paths += paths
            else:
                new_path_list = []
                for p in path_list:
                    np = p.copy()
                    np.append((i, j, DOWN))
                    new_path_list.append(np)
                candidate_nodes[(i, j, DOWN)] = Node(new_cost, paths, new_path_list)
        
    processed_nodes[current_node] = candidate_nodes[current_node]
    del candidate_nodes[current_node]

    # print(processed_nodes)
    # print(candidate_nodes)
