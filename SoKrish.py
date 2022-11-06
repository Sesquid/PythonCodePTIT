import math

t = int(input())
for i in range(t):
    res = 0
    n = input()
    for i in n:
        res += math.factorial(int(i))
    if int(n) == res:
        print("Yes")
    else: print("No")