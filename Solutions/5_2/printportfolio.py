# printportfolio.py

import logconfig
import readport

a = readport.read_portfolio("../../Data/portfolio3.dat")
for s in a:
    print(s)
