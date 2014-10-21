# rideindex.py
#
# Build an index mapping routes to all ride data reported for that route

import readrides
from collections import defaultdict

# Read all of the ride data
rides = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

# Build an index
route_index = defaultdict(list)

for ride in rides:
    route = ride['route']
    route_index[route].append(ride)

# Example, find maximum ridership on route 22
max_num_rides = 0
max_date = None
for ride in route_index['22']:
    if ride['numrides'] > max_num_rides:
        max_num_rides = ride['numrides']
        max_date = ride['date']

print("Maximum daily rides:", max_num_rides)
print("Date:", max_date)

