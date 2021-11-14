# Project Euler --> https://projecteuler.net/problem=18
# Problem 18 : Maximum path sum I

with open('p18_triangle.txt') as file:
    triangle = [list(map(int, line.split())) for line in file.read().split('\n')]

while len(triangle) != 1:
    for i in range(len(triangle) - 1):
        triangle[-2][i] += max(triangle[-1][i], triangle[-1][i + 1])
    del triangle[-1]

print(triangle[0][0])
