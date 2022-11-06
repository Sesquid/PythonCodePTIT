t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    k %= n
    a = list(map(int, input().split()))
    for i in range(k, n):
        print(a[i], end=' ')
    for i in range(0, k):
        print(a[i], end=' ')
    print()