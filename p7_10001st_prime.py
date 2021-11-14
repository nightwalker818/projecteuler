# Project Euler --> https://projecteuler.net/problem=7
# Problem 7 : 10001st prime
# What is the 10001st prime number?

def isPrime(x):
    """ Returns True if prime else False"""
    for i in range(2,int(x**0.5)+1):
        if (x % i == 0):
            return False

    return True

x = 2
y = 1
while (y<10001):
    x+=1
    if isPrime(x):
        y+=1

print('The 10001th prime is: ' + str(x))
