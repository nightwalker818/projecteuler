# Project Euler --> https://projecteuler.net/problem=16
# Problem 16 : Power digit sum
#What is the sum of the digits of the number 2** 1000?

product = 2 ** 1000
result = [int(i) for i in str(product)]
print(sum(result))
