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
minN = math.inf
maxN= -1
for i in range(n):
    for j in range(m):
        minN = min(minN, a[i][j])
        maxN = max(maxN, a[i][j])
dis = maxN - minN
flag = 0
for i in range(n):
    if dis in a[i]:
        flag = 1
if flag == 1:
    print(dis)
    for i in range(n):
        for j in range(m):
            if a[i][j] == dis:
                print("Vi tri [{}][{}]".format(i, j))
if flag == 0: print("NOT FOUND")
