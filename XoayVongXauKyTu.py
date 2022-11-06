def count(a, b):
    if a == b:
         return 0
    cnt = 0
    for i in range(len(b)):
        b = b[1:] + b[0]
        cnt += 1
        if a == b:
            return cnt
    return -1

a, b = [], []
check = 1
res = 10 ** 9
n = int(input())
for i in range(n):
    tmp = input()
    a.append(tmp)
    b.append(''.join(sorted(tmp)))
for i in range(n - 1):
    if b[i] != b[i + 1]:
        check = 0
        break
for i in a:
    if check == 0:
        break
    s = 0
    for j in a:
        x = count(i, j)
        if x != -1:
            s += x
            # print(x)
        else:
            check = 0
            break
    if check == 0:
        break
    res = min(res, s)
if check == 1: print(res)
else: print(-1)