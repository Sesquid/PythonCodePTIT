n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
# print(a)
k = int(input())
up = 0
down = 0
for i in range(n):
    for j in range(n):
        if i < j:
            down += a[i][j]
        if i > j:
            up += a[i][j]
if abs(up - down) <= k:
    print("YES", abs(up - down), sep='\n')
else: print( "NO", abs(up - down), sep='\n')