import re

with open('input.txt', 'r') as f:
    rules_input, manuals_input = f.read().split('\n\n')

# store rules as a set of tuples
rules = set()
for rule in rules_input.split('\n'):
    r0, r1 = map(int, re.findall(r'\d+', rule))
    rules.add((r0, r1))


total = 0
for m in manuals_input.split('\n'):
    unsorted_update = list(map(int, re.findall(r'\d+', m)))

    # pull out only the rules that deal with pages in
    # current update
    sub_rules = set()
    for r in rules:
        if r[0] in unsorted_update and r[1] in unsorted_update:
            sub_rules.add(r)

    # create a list of pages in the ordering
    # described by the subrules
    page_numbers = unsorted_update.copy()
    sorted_update = []
    while len(page_numbers) > 1:

        for n in page_numbers:
            leading_page = True
            for r in sub_rules:
                if n == r[1]:
                    leading_page = False
                    break
            if leading_page:
                break
        page_numbers.remove(n)
        sorted_update.append(n)

        # remove all rules containing n
        new_sub_rules = set()
        for r in sub_rules:
            if r[0] != n:
                new_sub_rules.add(r)
        sub_rules = new_sub_rules
    sorted_update.append(page_numbers.pop())

    if sorted_update != unsorted_update:
        total += sorted_update[len(sorted_update) // 2]
print(total)
