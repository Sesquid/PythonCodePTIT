t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    flag = 1;
    for i in range(n):
        if a[i] > b[i]:
            flag = 0
            break
    print("YES" if flag == 1 else "NO")
