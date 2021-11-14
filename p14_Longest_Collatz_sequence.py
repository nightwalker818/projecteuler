# Project Euler --> https://projecteuler.net/problem=14
# Problem 14 : Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?

def collatz_sequence(n):
    """ Calculates the collatz sequence of starting with n and return the length of it's term"""
    terms = [n]
    while True:
        if n % 2 == 0:
            n = n /2
        else :
            n = (n * 3) + 1
        terms.append(int(n))
        if terms[-1] == 1:
            break
    return len(terms)


def longest_chain():
    """ Calculates all possibilites for numbers under one million and returns starting number that produces the longes chain"""
    result = []
    for i in range(10000,1000000):
        x = collatz_sequence(i)
        result.append(x)
    m = int(result.index(max(result))) + 10000
    return print(m)

longest_chain()
