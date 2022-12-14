n = int(input())
a = [0] * (n + 1)
flag = 1
for i in range(n - 1):
    tmp = input().split()
    a[int(tmp[0])] += 1
    a[int(tmp[1])] += 1
for i in range(1, n + 1):
    if a[i] != 1 and a[i] != n - 1:
        print("No")
        flag = 0
        break
if flag == 1: print("Yes")