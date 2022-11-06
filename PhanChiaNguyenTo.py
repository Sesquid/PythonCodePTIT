import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

n = int(input())
a = [int(x) for x in input().split()]
b = {}
for i in a : b[i] = 1
a = list(b)
n = len(a)
for i in range(1, n) : a[i] += a[i - 1]
flag = 0
for i in range(n):
    if isPrime(a[i]) and isPrime(a[n - 1] - a[i]):
        print(i)
        flag = 1
        break
if flag == 0:
    print("NOT FOUND")