# Project Euler --> https://projecteuler.net/problem=9
# Problem 9 : Special Pythagorean triplet
#1. Find three numbers that are less than 1000
#2. The first two numbers must each equal in a pythagorean triplet.
#      2a. a**2 + b**2 = c**2
#3. Each number is smaller than the next. a < b < c
#4. The answer asks for the product of abc, which means to multiply a * b * c and print the result

for a in range(1,400):
    for b in range(1,400):
        c = 1000 - a - b
        if a < b < c:
            if c**2 == a**2 + b**2:
                print(a*b*c)
