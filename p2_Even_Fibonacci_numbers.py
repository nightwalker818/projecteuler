# Project Euler --> https://projecteuler.net/problem=2
# Problem 2 : Even Fibonacci numbers
# Find the sum of the even-valued terms of Fibonacci sequence whose values do not exceed four million.
# Updated Faster solution
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# We will be using tuple and swaping the variables to same storage and time
# I am trying to improve my code to get a faster result and saving storage by using a tuple and swaping variables
import time
start_time = time.time()

def fibEvenSum():
    i = 2
    sumEvenValues = 0
    fib1,fib2 = (0,1)
    nextValue = 0
    while (nextValue < 4000000):
        nextValue = fib1+ fib2
        fib1,fib2 = (fib2,nextValue)
        
        if nextValue % 2 == 0:
            sumEvenValues += nextValue
        
        i += 1
    return sumEvenValues


print(fibEvenSum())
        

# answer needs to be 4613732
# My program took 0.00033664703369140625 to run
