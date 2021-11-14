# Project Euler --> https://projecteuler.net/problem=6
# Problem 6 : Sum square difference
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import math

def difference_sums_squares():
    """Calculates the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum """
    sum_of_the_squares = 0
    the_sums = 0
    for i in range(1, 101):
        sum_of_the_squares += math.pow(i,2)
        the_sums += i

    square_of_the_sum = the_sums**2
    return square_of_the_sum - sum_of_the_squares

print(difference_sums_squares())
