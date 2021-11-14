# Project Euler --> https://projecteuler.net/problem=12
# Problem 12 : Highly divisible triangular number
#STEP 1: We want to create a function that calculates the first 7 triangular
#STEP 2: Create a function that returns the factors of each traingular
#STEP 3: store the length of the factors and when reach to to 500 print the triangular

def triangular(n):
    """ Calculate the nth triangular"""
    triang = n * (n + 1) / 2
    return triang


def factors(x):
    """Calculate the number of divisors and return the number if divisor"""
    j = []
    for i in range(1,int(x**0.5) + 1):
        if x % i == 0:
            if(i != x/i):
                j.append(i)
                j.append(x/i)
            else:
                j.append(i)
    return len(j)

def result():
    """Calculates the first triangle number that has 500 or above divisors """
    n = 500
    while True:
        x = triangular(n)
        z = factors(int(x))
        if z >= 500:
            break
        else:
            n += 1
    return x

m = result()
print(m)
