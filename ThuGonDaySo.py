n = int(input())
a = [int(x) for x in input().split()]
l = list()
for i in range(n):
    if len(l) == 0 or (l[-1] + a[i]) % 2 == 1:
        l.append(a[i])
    elif len(l) > 0: l.pop()
print(len(l))
