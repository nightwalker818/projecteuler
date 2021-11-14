# Project Euler --> https://projecteuler.net/problem=15
# Problem 15 : Lattice paths
# To use the factorial() we need to import math
#How many such routes are there through a 20×20 grid?
#To solve this problem we used Pascal's Triangle formala
# check out https://www.mathsisfun.com/pascals-triangle.html

import math
n = 20
result = math.factorial(n * 2) / math.factorial(n) ** 2
print (result)
