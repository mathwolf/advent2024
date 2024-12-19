import re

def build_design(design):
    # recursively try to build input
    # return 1 if possible, 0 if not possible

    for p in patterns:
        if re.match(p, design):
            if len(p) == len(design):
                return 1
            if build_design(design[len(p):]):
                return 1
    return 0

with open('input.txt', 'r') as f:
    in1, in2 = f.read().split('\n\n')
    
patterns = re.findall(r'\w+', in1)

total = 0
for design in in2.split('\n'):
    total += build_design(design)
print(total)
