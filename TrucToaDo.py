t = int(input())
for i in range(t):
    n = int(input())
    l = list()
    for i in range(n):
        pair = tuple(map(int, input().split()))
        l.append(pair)
    l = sorted(l, key=lambda x: (x[1]))
    cnt = 0
    k = -1
    for i in l:
        if i[0] >= k:
            cnt += 1
            k = i[1]
    print(cnt)

