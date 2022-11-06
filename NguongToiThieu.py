s = input()
k = int(input())
a = {}
for i in range(0, len(s), 2):
    tmp = s[i:i + 2]
    if len(tmp) == 2:
        if not tmp in a:
            a[tmp] = 1
        else: a[tmp] += 1
b = [[int(i), a[i]] for i in a]
b.sort()
flag = 0
for i in b:
    if i[1] >= k:
        flag = 1
        print(i[0], i[1])
if flag == 0: print("NOT FOUND")