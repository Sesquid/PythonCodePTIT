t = int(input())

for z in range(t):
    n, m = map(int, input().split())
    a = [[int(x) for x in input().split()] for x in range(n)]
    b = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(n):
            print(c[i][j], end=' ')
        print()

