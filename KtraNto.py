import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

n, m = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
    for i in a:
        print(1 if isPrime(i) else 0, end=' ')
    print()
