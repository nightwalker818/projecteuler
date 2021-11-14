# Project Euler --> https://projecteuler.net/problem=104
# Problem 104 : Pandigital Fibonacci ends

import itertools

def pandigital_fib_ends():
	""" Checks if the first and last 9 digits are pandigital  """
	x = 10**9
	a = 0
	b = 1
	for i in itertools.count():
		if ''.join(sorted(str(a))) == '123456789':  # If last nine digits are 1-9 pandigital
			f = fib(i)[0]
			if ''.join(sorted(str(f)[ : 9])) == '123456789':  # If first nine digits are 1-9 pandigital
				print(i)
				break
		a, b = b, (a + b) % x # a = f(i) % x b = f(i+1) % x


# Returns the tuple (F(n), F(n+1)), computed by the fast doubling method.
def fib(n):
	""" Calculates the nth Fibonacci """
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * (b * 2 - a)
        d = a**2  + b**2
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

pandigital_fib_ends()
