# pcost.py

total_cost = 0.0

f = open('../../Data/portfolio.dat', 'r')
for line in f:
    fields = line.split()
    nshares = int(fields[1])
    price = float(fields[2])
    total_cost = total_cost + nshares * price
f.close()

print(total_cost)
