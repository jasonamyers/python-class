# yearlyrides.py
#
# Build an index of yearly bus ridership

import readrides
from collections import defaultdict, Counter

rides = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

yearly_ridership = defaultdict(Counter)
for ride in rides:
    month, day, year = ride['date'].split('/')
    yearly_ridership[year][ride['route']] += ride['numrides']
