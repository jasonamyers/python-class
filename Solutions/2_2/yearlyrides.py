# yearlyrides.py
#
# Build an year-route index of bus ridership

import readrides

rides = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

yearly_ridership = { }
for ride in rides:
    month, day, year = ride['date'].split('/')
    if year not in yearly_ridership:
        yearly_ridership[year] = { }

    year_route_totals = yearly_ridership[year]
    if ride['route'] not in year_route_totals:
        year_route_totals[ride['route']] = 0
    year_route_totals[ride['route']] += ride['numrides']

# Examples
print(yearly_ridership['2011']['22'])
print(yearly_ridership['2001']['22'])
print((yearly_ridership['2011']['22'] - yearly_ridership['2001']['22']))

# For memory use. Run with python -i
import os
print(os.getpid())
