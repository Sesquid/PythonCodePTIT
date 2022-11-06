import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t = int(input())
for i in range(t):
    n = input()
    m = list(n)
    m.reverse()
    m = int(''.join(m))
    s = 0
    flag = 1
    for i in n:
        s += int(i)
        if not isPrime(int(i)):
            flag = 0
            break
    if isPrime(int(n)) and isPrime(m) and flag == 1:
        print("Yes")
    else: print("No")
    