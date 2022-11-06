t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else: d[i] = 1
    for i in d:
        if d[i] % 2 == 1:
            print(i)
            break