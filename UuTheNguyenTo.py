import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t = int(input())
for i in range(t):
    n = input()
    cnt = 0
    for i in n:
        if isPrime(int(i)): cnt += 1
        else: cnt -= 1
    if isPrime(len(n)) and cnt > 0:
        print("YES")
    else: print("NO")