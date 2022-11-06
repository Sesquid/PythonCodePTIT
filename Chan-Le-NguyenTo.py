import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    res = 0
    for i in range(len(n)):
        res += int(n[i])
        if i % 2 == 0 and int(n[i]) % 2 != 0 or i % 2 == 1 and int(n[i]) % 2 != 1:
            return False
    if isPrime(res): return True
    return False


t = int(input())

for i in range(t):
    n = input()
    print("YES" if check(n) else "NO")

