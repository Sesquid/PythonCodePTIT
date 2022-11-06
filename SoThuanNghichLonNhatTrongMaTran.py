import math


def check(n):
    s = list(str(n))
    s.reverse()
    s = int(''.join(s))
    if s == n: return True
    return False

n, m = map(int, input().split())
a = [[int(i) for i in input().split()]for j in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if check(a[i][j]) and a[i][j] > res:
            res = a[i][j]
if res < 11: print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print("Vi tri [{}][{}]".format(i, j))
