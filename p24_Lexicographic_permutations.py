# Project Euler --> https://projecteuler.net/problem=24
# Problem 24 : Lexicographic permutations

from math import factorial

digits = [0,1,2,3,4,5,6,7,8,9]
result = []
index = 999999

for j in range(9,-1,-1):
    n = int(index/factorial(j))
    result.append(str(digits[n]))
    index -= n*factorial(j)
    del digits[n]

print(''.join(result))
