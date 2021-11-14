# Project Euler --> https://projecteuler.net/problem=41
# Problem 41 : Pandigital prime
# What is the largest n-digit pandigital prime that exists?

def isPrime(x):
    """ Returns True if prime else False"""
    for i in range(2,int(x**0.5)+1):
        if (x % i == 0):
            return False

    return True

def isPandigital(x):
    """ Returns True if Pandigital """
    abc =[str(i) for i in range(1,len(str(x))+1)]
    if sorted(str(x)) == abc:
        return True

for i in range(7654321,2143,-1):
    if isPrime(i) and isPandigital(i):
            print(i)
            break
