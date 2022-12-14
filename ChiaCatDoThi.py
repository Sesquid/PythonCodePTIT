ke = {}

def DFS(ke, used, u):
    used[u] = 1
    for i in ke[u]:
        if used[i] == 0:
            DFS(ke, used, i)

t = int(input())
for x in range(t):
    res = 0
    ans = 10**10
    n, m = map(int, input().split())
    for i in range(m):
        u, v = map(int, input().split())
        if u not in ke:
            ke[u] = []
        if v not in ke:
            ke[v] = []
        ke[u] += [v]
        ke[v] += [u]
    for i in range(n - 1, 0, -1):
        used = [0] * (n + 1)
        used [i] = 1
        cnt = 0
        for j in range(1, n + 1):
            if used[j] == 0: 
                cnt += 1
                DFS(ke, used, j)
        if cnt > 1 and cnt >= res:
            res == cnt
            ans = i 
        if ans == 10 ** 10: 
            ans = 0
    print(ans)
