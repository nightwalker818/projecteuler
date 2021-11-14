# Project Euler --> https://projecteuler.net/problem=1
# Problem 1 : Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000
total = 0
for x in range(1000):
    if (x % 3 == 0) or (x % 5 == 0):
        total += x

print(total)
