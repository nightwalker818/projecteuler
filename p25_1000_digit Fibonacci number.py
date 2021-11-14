# Project Euler --> https://projecteuler.net/problem=25
# Problem 25 : 1000-digit Fibonacci number

def fib(n):
    if n ==1 or n == 2:
        return 1

    fib_s = [None] * (n + 1)
    fib_s[1] = 1
    fib_s[2] = 1

    for i in range (3,n+1):
        fib_s[i] = fib_s[i-1] + fib_s[i-2]
    return fib_s[n]


for i in range(4500,5000):
    n = fib(i)
    if len(str(n)) == 1000:
        print(i)
        break
    
