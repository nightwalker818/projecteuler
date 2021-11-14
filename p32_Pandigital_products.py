# Project Euler --> https://projecteuler.net/problem=32
# Problem 32 : Pandigital products

result =set()
for i in range(1234,9877):
    for j in range(2,int(i**0.5) + 1):
        if i % j ==  0:
            if''.join(sorted('%d%d%d' % (i,j,i//j))) == '123456789':
                result.add(i)

print(sum(result))
