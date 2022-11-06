import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

n, m = map(int, input().split())
a = [[int(i) for i in input().split()]for j in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]) and a[i][j] > res:
            res = a[i][j]
if res == 0: print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print("Vi tri [{}][{}]".format(i, j))
