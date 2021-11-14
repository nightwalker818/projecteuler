# Project Euler --> https://projecteuler.net/problem=21
# Problem 21 : Amicable numbers
# Evaluate the sum of all the amicable numbers under 10000
# since d(b) = a and d(a) = b and a!=b the d(d(a)) = a

def d(n):
    """Calculate the sum of divisors of n """
    j = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if(i != n/i and n/i != n):
                j.append(i)
                j.append(n/i)
            else:
                j.append(i)

    return sum(j)

total = [a for a in range(1,10001) if ( a == d(d(a))  and a != d(a))]
print(sum(total))
