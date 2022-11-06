import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

n = int(input())
a = [int(x) for x in input().split() ]
b = sorted([x for x in a if isPrime(x)])
ind = 0
for i in a:
    if isPrime(i):
        print(b[ind], end=' ')
        ind += 1
    else: print(i, end=' ')



