import csv
import read_rides_as_dict
from collections import defaultdict


def read_rides(filename):
    f = open(filename)
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rides = defaultdict(list)
    for row in f_csv:
        route = row[0]
        date = row[1]
        numrides = int(row[3])
        rides[route].append((date, numrides))
    f.close()
    return rides

if __name__ == '__main__':
    rides = read_rides('Data/ctabus.csv')
    max_rides = 0
    max_rides_date = None
    for date, numrides in rides['22']:
        if numrides > max_rides:
            max_rides = numrides
            max_rides_date = date
    print('Maximum daily rides:', max_rides)
    print('Date:', max_rides_date)
