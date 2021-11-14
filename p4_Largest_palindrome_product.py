# Project Euler --> https://projecteuler.net/problem=4
# Problem 4 : Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

n = 0
for a in range(999, 100, -1):
    for b in range(a, 500, -1):# i used 500 to save time and avoid duplication
        x = a * b
        if x > n: # we check if x is palindrome and if it is we will store it in n
            s = str(x)
            if s == s[::-1]:
                n = x
print(n)
