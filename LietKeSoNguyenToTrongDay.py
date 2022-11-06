import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    if isPrime(i):
        if i in d:
            d[i] += 1
        else: d[i] = 1
for i in d:
    print(i, d[i])

