# fieldparse.py

def parse(lines,types,names):
    records = []
    for line in lines:
        # Split into fields
        fields = line.split()

        # Apply conversions to each field
        row = [func(val) for func, val in zip(types, fields) ]

        # Create a dictionary from the data
        record = dict(zip(names,row))

        records.append(record)
    return records
