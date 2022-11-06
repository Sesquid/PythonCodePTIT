a = ['0', '2', '4', '6', '8']
res = []
def Try(s, res):
    k = list(s)
    k.reverse()
    k = int(s + ''.join(k))

    res.append(k)
    if len(s) < 3:
        for i in a:
            Try(s + i, res)
for i in range (1, 5): Try(a[i], res)
res.sort()
t = int(input())
for i in range (t):
    n = int(input())
    for j in res:
        if j < n: print(j, end=' ')
    print()
