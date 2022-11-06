import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t = int(input())


for i in range(t):
    n = input()
    s1 = n[:3]
    s2 = n[-3:]
    print("YES" if isPrime(int(s1)) and isPrime(int(s2)) else "NO")
