import collections
t = int(input())
for i in range(t):
    n = int(input())
    q = collections.deque()
    a = list(map(int, input().split()))
    for i in range(n):
        while q and a[q[-1]] <= a[i]: q.pop()
        if q: print(i - q[-1], end=' ')
        else: print(i + 1, end=' ')
        q.append(i)
        # print(q)
    print()

