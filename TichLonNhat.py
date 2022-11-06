import math

n = int(input())
a = sorted(list(map(int, input().split())))
res = -math.inf
x = a[0] * a[1]
y = a[0] * a[1] * a[-1]
z = a[-3] * a[-2] * a[-1]
q = a[-2] * a[-1]
res = max(res, x, y, z, q)
print(res)