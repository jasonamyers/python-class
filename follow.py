import os
import time

def follow(filename):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)   # Sleep briefly and retry
                continue
            yield line

    #fields = line.split(',')
    #name = fields[0].strip('"')
    #price = float(fields[1])
    #change = float(fields[4])
    #if change < 0:
        #print('%10s %10.2f %10.2f' % (name, price, change))

def splitter(lines):
    for line in lines:
        yield line.split(',')

def make_records(rows,names):
    for row in rows:
        yield dict(zip(names,row))

def unquote(records,keylist):
    for r in records:
        for key in keylist:
            r[key] = r[key].strip('"')
        yield r

# Perform a type conversion on selected fields
def convert(records,converter,keylist):
    for r in records:
        for key in keylist:
            r[key] = converter(r[key])
        yield r

def parse_stock_data(lines):
    rows = splitter(lines)
    records = make_records(rows, ['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume'])
    records = unquote(records, ['name', 'date', 'time'])
    records = convert(records, float, ['price', 'change', 'open', 'high', 'low'])
    records = convert(records, int, ['volume'])
    return records
