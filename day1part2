import re

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

first_list = []
second_list = []
for L in lines:
    n1, n2 = re.findall(r'\d+', L)
    first_list.append(int(n1))
    second_list.append(int(n2))

total = 0
for n in first_list:
    total += n * second_list.count(n)
print(total)
