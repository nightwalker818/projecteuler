# Project Euler --> https://projecteuler.net/problem=62
# Problem 62 : Cubic permutations


# list of cubes converted to string and sorted,10000 is our range since we looking for 5 digits at least,
cubes = [sorted(str(i**3)) for i in range(10000)]
# list of the counts of occurrence of each value in cubes
counts = [cubes.count(i) for i in cubes]
# prints the cube of  index of the first occurence specified value
print(counts.index(5)**3)
