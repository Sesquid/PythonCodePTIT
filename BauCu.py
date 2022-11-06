a = [0] * 11
n, m = map(int, input().split())
for i in input().split():
    a[int(i)] += 1


ans = 0
res = -1
nMax = max(a)
for i in range(m, 0, -1):
    if res <= a[i] < nMax:
        res = a[i]
        ans = i
if res == -1 or res == 0: print("NONE")
else: print(ans)