import math


t = int(input())
def isPrime(n):
    for i in range (2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

while t > 0:
    t -= 1
    n = int(input())
    count = 0
    for i in range (1, n):
        if math.gcd(i, n) == 1 : count += 1
    print("YES" if isPrime(count) else "NO")
