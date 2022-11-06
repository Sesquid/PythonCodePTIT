t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    res = "NO"
    for i in a:
        if i in d: d[i] += 1
        else: d[i] = 1
        if d[i] > n / 2: res = i
    print(res)
