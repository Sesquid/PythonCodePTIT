t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    nr = list(map(int, input().split()))
    mr = list(map(int, input().split()))
    kr = list(map(int, input().split()))
    x = 0; y = 0; z = 0
    flag = 0
    while x < n and y < m and z < k:
        if nr[x] == mr[y] == kr[z]:
            flag = 1
            print(nr[x], end=' ')
            x += 1; y += 1; z += 1
        elif mr[y] < nr[x]: y += 1
        elif kr[z] < mr[y]: z += 1
        else: x += 1
    print()
    if flag == 0: print("NO")
