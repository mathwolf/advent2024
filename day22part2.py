def mix(val, sn):
    return val ^ sn

def prune(sn):
    return sn % 16777216

with open('input.txt', 'r') as f:
    numbers = f.read().split('\n')

TURNS = 2000
total_sales = {}
for n in numbers:
    n = int(n)
    price = n % 10
    current_price_seq = []
    individual_sales = {}
    for t in range(TURNS):
        n = mix(64*n, n)
        n = prune(n)
        n = mix(n//32, n)
        n = prune(n)
        n = mix(n*2048, n)
        n = prune(n)

        new_price = n % 10
        delta_p = new_price - price
        price = new_price

        if len(current_price_seq) != 4:
            current_price_seq.append(delta_p)
        else:
            current_price_seq.pop(0)
            current_price_seq.append(delta_p)
            if tuple(current_price_seq) not in individual_sales.keys():
                individual_sales[tuple(current_price_seq)] = price

      for k in individual_sales.keys():
        if k in total_sales.keys():
            total_sales[k] = individual_sales[k] + total_sales[k]
        else:
            total_sales[k] = individual_sales[k]

print(max(total_sales.values()))
