import math


def isPrime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

t= int(input())
for i in range(t):
    s = input()
    cnt = 0
    if int(s) < 1: print("NO")
    elif (isPrime(len(s))):
        for i in s:
            if i == '2' or i == '3' or i == '5' or i =='7':
                cnt += 1
        if cnt > len(s) - cnt: print("YES")
        else: print("NO")
    else: print("NO")


