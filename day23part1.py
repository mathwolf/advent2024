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

total = 0
doubles = 0
triples = 0
for c in computers.keys():
    if c[0] != 't':
        continue
    for c1, c2 in combinations(computers[c], 2):
        if c1 in computers[c2]:
            if c1[0] == 't':
                if c2[0] == 't':
                    triples += 1
                else:
                    doubles += 1
            else:
                if c2[0] == 't':
                    doubles += 1
            total += 1
print(total - doubles // 2 - 2 * triples // 3)
