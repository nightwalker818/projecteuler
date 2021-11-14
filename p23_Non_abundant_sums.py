# Project Euler --> https://projecteuler.net/problem=23
# Problem 23 : Non-abundant sums

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

"""Calculate abundant numbers """
abundant = set()
for i in range(12,28123):
    if d(i) > i:
        abundant.add(i)

result = 0
for n in range(28123):
    for i in abundant:
        if n - i in abundant:
            break
    else:
        result += n

print(result)
