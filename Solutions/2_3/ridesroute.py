# ridesroute.py
#
# Tabulate and print out the total number of rides by route

import readrides
from collections import Counter

# Read all of the ride data
rides = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

# Tabulate
rides_per_route = Counter()

for ride in rides:
    route = ride['route']
    rides_per_route[route] += ride['numrides']

print('Route Rides')
print('===== ==========')
for route, count in rides_per_route.most_common(10):
    print('%-5s %d' % (route, count))



