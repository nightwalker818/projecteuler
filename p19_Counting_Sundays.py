# Project Euler --> https://projecteuler.net/problem=19
# Problem 19 : Counting Sundays
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

total=0
for yy in range(1901, 2001):
    for mm in range(1,13):
        x =  datetime.datetime(yy, mm, 1)
        if x.strftime('%A')=='Sunday':
            total+=1

print(total)
