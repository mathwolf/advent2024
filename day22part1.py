def mix(val, sn):
    return val ^ sn

def prune(sn):
    return sn % 16777216

with open('input.txt', 'r') as f:
    numbers = f.read().split('\n')

TURNS = 2000
total = 0
for n in numbers:
    for t in range(TURNS):
        n = int(n)
        n = mix(64*n, n)
        n = prune(n)

        n = mix(n//32, n)
        n = prune(n)

        n = mix(n*2048, n)
        n = prune(n)
    total += n
print(total)
