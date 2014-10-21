# readport.py

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        for line in f:
            fields = line.split()
            record = {
                'name' : fields[0], 
                'shares' : int(fields[1]),
                'price' : float(fields[2])
                }
            portfolio.append(record)
    return portfolio
