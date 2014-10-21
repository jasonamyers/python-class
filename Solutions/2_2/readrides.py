# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route = row[0]
        date = row[1]
        daytype = row[2]
        numrides = int(row[3])
        ride = (route, date, daytype, numrides)
        rides.append(ride)
    f.close()
    return rides

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route = row[0]
        date = row[1]
        daytype = row[2]
        numrides = int(row[3])
        ride = {
            'route': route, 
            'date': date, 
            'daytype': daytype, 
            'numrides' : numrides
            }
        rides.append(ride)
    f.close()
    return rides

class Ride(object):
    # Uncomment to see effect of slots
    # __slots__ = ('route', 'date', 'daytype', 'numrides')
    def __init__(self, route, date, daytype, numrides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.numrides = numrides

# Uncomment to use a namedtuple instead
#from collections import namedtuple
#Ride = namedtuple('Ride',('route','date','daytype','numrides'))

def read_rides_as_instances(filename):
    '''
    Read the bus ride data as a list of instances
    '''
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route = row[0]
        date = row[1]
        daytype = row[2]
        numrides = int(row[3])
        ride = Ride(route, date, daytype, numrides)
        rides.append(ride)
    f.close()
    return rides

if __name__ == '__main__':
    import os
    read_rides = read_rides_as_tuples # Change to as_dicts, as_instances, etc.
    rides = read_rides('../../Data/ctabus.csv')
    print('Look at memory use of PID', os.getpid())
