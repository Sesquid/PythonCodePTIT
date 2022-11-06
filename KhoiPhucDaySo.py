n = int(input())
res = [0] * n
a = [[int(x) for x in input().split()] for k in range(n)]
if n == 2: res = [a[0][1] // 2, a[0][1] - a[0][1] // 2]
else:
    suma = sum(sum(x) for x in a)
    sumRes = suma // (2 * (n - 1))
    for i in range(n):
        res[i] = (sum(a[i]) - sumRes) // (n - 2)
for i in res:
    print(i, end=' ')