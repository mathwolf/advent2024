import re

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

first_list = []
second_list = []
for L in lines:
    n1, n2 = re.findall(r'\d+', L)
    first_list.append(int(n1))
    second_list.append(int(n2))

first_list.sort()
second_list.sort()

total = 0
for t in zip(first_list, second_list):
    total += abs(t[0] - t[1])
print(total)
