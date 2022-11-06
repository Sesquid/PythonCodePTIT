import math

t = int(input())
for i in range (t):
    n = input()
    m = list(n)
    m.reverse()
    n = int(n)
    m = int(''.join(m))
    if math.gcd(m, n) == 1: print("YES")
    else: print("NO")

