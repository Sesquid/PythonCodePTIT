s = input()
a = {}
for i in range(0, len(s), 2):
    tmp = s[i:i + 2]
    if len(tmp) == 2:
        a[tmp] = 1

for i in a:
    print(i, end=' ')