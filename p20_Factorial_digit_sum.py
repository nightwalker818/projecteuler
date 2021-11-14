# Project Euler --> https://projecteuler.net/problem=20
# Problem 20 : Factorial digit sum
# Find the sum of the digits in the number 100!

import math

p =  math.factorial(100)
result = [int(i) for i in str(p)]
print(sum(result))
