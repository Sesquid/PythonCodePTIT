import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t = int(input())
for i in range(t):
    s = input()
    sum = 0
    for j in s:
        sum += int(j)
    if isPrime(sum):
        print("YES")
    else: print("NO")