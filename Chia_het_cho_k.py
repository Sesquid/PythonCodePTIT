a, k, n = map(int, input().split())
b = k - a % k + a
if b > n: print(-1)
else:
    for i in range(b, n + 1, k):
        print(i - a, end = ' ')
