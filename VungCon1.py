dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def DFS(i, j, a, n, m):
    a[i][j] = 0
    for x in dir:
        u = i+x[0]
        v = j+x[1]
        if u >= 0 and u < n and v >= 0 and v < m and a[u][v] == 1:
            DFS(u, v, a, n, m)


n, m = map(int, input().split())
a = [[int(i) for i in input().split()] for j in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            ans += 1

            DFS(i, j, a, n, m)
print(ans)
