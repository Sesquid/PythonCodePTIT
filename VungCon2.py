dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
res = 0


def dfs(i, j, a, n, m, sum):
    global res
    res = max(sum, res)
    a[i][j] = 0
    for x in dir:
        u = i + x[0]
        v = j + x[1]
        if 0 <= u < n and 0 <= v < m and a[u][v] == 1:
            dfs(u, v, a, n, m, sum + 1)


n, m = map(int, input().split())
a = [[int(i) for i in input().split()] for j in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            DFS(i, j, a, n, m, 1)
print(res)
