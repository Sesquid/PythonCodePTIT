n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
k = int(input())
up = 0
down = 0
for i in range(n):
    for j in range(n):
        if i + j + 1 < n: up += a[i][j]
        elif i + j + 1 > n: down += a[i][j]
print("YES" if abs(up - down) <= k else "NO", abs(up - down), sep='\n')