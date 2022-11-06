import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    for i in range(len(n)):
        if isPrime(i) and not isPrime(int(n[i])) or not isPrime(i) and isPrime(int(n[i])):
            return False
    return True

t = int(input())
for i in range(t):
    n = input()
    print("YES" if check(n) else "NO")
