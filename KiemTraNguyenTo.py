import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t= int(input())
for i in range (t):
    s = input()
    s = list(s[-4:])
    s = int(''.join(s))
    print("YES" if isPrime(s) else "NO")
