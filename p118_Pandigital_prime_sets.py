# Project Euler --> https://projecteuler.net/problem=118
# Problem 118 : Pandigital Prime Sets
# How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

from itertools import permutations

def isprime(x):
    """ Returns True if prime else False"""
    if x < 2:
        return False
    for i in range(2,int(x**0.5)+1):
        if (x % i == 0):
            return False
    return True


def p118(c = 0, p = [], d = set('123456789')):
    """ Returns the number of sets with primes elements"""
    if not d:
        c += 1
    else:
        for i in range(1, len(d) + 1):
            for x in permutations(d, i):
                y = int(''.join(x))
                if y > 1 and (not p or y > p[-1]) and isprime(y):
                    c = p118(c, p + [y], d - set(x))

    return c

print(p118())
