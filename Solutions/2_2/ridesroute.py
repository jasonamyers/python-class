# ridesroute.py
#
# Tabulate and print out the total number of rides by route

import readrides

# Read all of the ride data
rides = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

# Tabulate
rides_per_route = { }

for ride in rides:
    route = ride['route']
    if route not in rides_per_route:
        rides_per_route[route] = 0
    rides_per_route[route] += ride['numrides']

print('Route Rides')
print('===== ==========')
for route in sorted(rides_per_route):
    print('%-5s %d' % (route, rides_per_route[route]))

