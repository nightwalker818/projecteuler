# Project Euler --> https://projecteuler.net/problem=3
# Problem 3 : Largest prime factor
# Finding the largest prime factor of the number 600851475143
allfactors =[]
prime_factors = []

x = 600851475143
r = int((x**0.5)+1)
print(r)
#we first create a list of all factores of the square root of 600851475143
for n in range(2,r):
    if x % n == 0:
        allfactors.append(n)
#function to test weather it is prime or not
def test_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2,x):
            if(x % n == 0):
                return False
        return True
#we create a list of the prime fatores of 600851475143
for y in allfactors:
    if test_prime(y):
        prime_factors.append(y)

# we get the maximum value from the prime factor list we created
print(max(prime_factors))
