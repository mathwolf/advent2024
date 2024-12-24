import re
from itertools import combinations

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

computers = {}
for L in lines:
    c1, c2 = re.findall(r'\w+', L)
    if c1 in computers.keys():
        computers[c1].add(c2)
    else:
        computers[c1] = {c2}
    if c2 in computers.keys():
        computers[c2].add(c1)
    else:
        computers[c2] = {c1}

# for each computer, we define the "weight" by calculating
# the number of pairs of connects that are themselves
# connected
computers_by_weight = []
for k in computers.keys():
    # find pairs of connections
    total = 0
    for c, d in combinations(computers[k], 2):
        if d in computers[c]:
            total += 1
    computers_by_weight.append((k, total))

# format output, there is a group of nodes with weight 66
output_list = []
for c in computers_by_weight:
    if c[1] == 66:
        output_list.append(c[0])
output_list.sort()
outstr = ''
for n in output_list:
    outstr += n + ','
print(outstr[:-1])
