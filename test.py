n = int(input())
a = [0] * (n + 1)
for i in range (1, n) :
    tmp = list(map(int, input().split()))
    a[tmp[0]] += 1
    a[tmp[1]] += 1
# print(a)
flag = 1
for i in range(1, n + 1):
    if(a[i] != 1 and a[i] != n - 1):
        flag = 0
        break
print("Yes" if flag == 1 else "No")