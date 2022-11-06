t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(a.index(max(a)), k)
    for i in a:
        if i < 0: print(i, end=' ')
    for i in a:
        if i >= 0: print(i, end=' ')
    print()
