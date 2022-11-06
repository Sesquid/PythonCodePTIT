import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

a = list()

tmp = 2
while len(a) != 1100:
    if isPrime(tmp): a.append(tmp)
    tmp += 1
n, x = map(int, input().split())
for i in range(n + 1):
    print(x, end=' ')
    x += a[i]
