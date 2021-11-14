# Project Euler --> https://projecteuler.net/problem=38
# Problem 38 : Pandigital multiples

for i in range(9387,9234,-1):
    result = str(i) + str(i*2)
    if  ''.join(sorted(result)) == '123456789':
        break
print(result)
