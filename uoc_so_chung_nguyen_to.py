import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1


t = int(input())
while t > 0:
    t -= 1
    a, b = map(int, input().split(" "))
    res = math.gcd(a, b)
    tmp = 0
    while res > 0:
        tmp += res % 10
        res //= 10
    print("YES" if isPrime(tmp) else "NO")