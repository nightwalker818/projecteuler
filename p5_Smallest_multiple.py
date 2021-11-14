# Project Euler --> https://projecteuler.net/problem=5
# Problem 5 : Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallest_multiple(n):
    i = 2520
    while True:
        for a in range(n, 10, -1):
            if i % a != 0:
                i += 2520
                break
            if(a == 11 and i % a == 0):
                return i

print(smallest_multiple(20))
