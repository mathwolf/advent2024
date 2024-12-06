import re

with open('input.txt', 'r') as f:
    rules_input, manuals_input = f.read().split('\n\n')

# store rules as a set of tuples
rules = set()
for rule in rules_input.split('\n'):
    r0, r1 = re.findall(r'\d+', rule)
    rules.add((int(r0), int(r1)))

total = 0
for m in manuals_input.split('\n'):
    page_order = list(map(int, re.findall(r'\d+', m)))
    page_order_valid = True
    for r in rules:
        if r[0] in page_order and r[1] in page_order \
            and page_order.index(r[1]) < page_order.index(r[0]):
                    page_order_valid = False
                    break
    if page_order_valid:
        total += page_order[len(page_order) // 2]
print(total)
