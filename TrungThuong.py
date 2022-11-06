t = int(input())
for i in range(t):
    a = {}
    n = int(input())
    res = -1
    ans = 10 ** 20
    for i in range(n):
        x = int(input())
        if a.get(x):
            a[x] += 1
        else: a[x] = 1
    # print(a)
    for i in a:
        if a[i] > res:
            res = a[i]
            ans = i
        elif a[i] == res:
            ans = min(i, ans)
    print(ans)

