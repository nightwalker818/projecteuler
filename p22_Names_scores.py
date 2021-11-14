# Project Euler --> https://projecteuler.net/problem=22
# Problem 22 : Names scores
# A is 65 in the unicode table

with open('p022_names.txt') as file:
    names = file.read().replace('"','').split(',')
    names.sort()

a = []
for index,name in enumerate(names, start=1):
    b = []
    for char in name:
        b.append(ord(char) - 64)
    a.append(sum(b)*index)

print(sum(a))
