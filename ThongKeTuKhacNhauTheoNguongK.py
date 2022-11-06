import re

n, k = map(int, input().split())
a = []
d = {}
for i in range(n):
    s = input().lower()
    s = re.split('[^\\w\\d]', s)
    a += s
for i in a:
    if i != '':
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
a = [[i.lower(), d[i] ] for i in d]
a = sorted(a, key=lambda x: (-x[1], x[0]))
for i in range( len(a)):
    if a[i][1] >= k:
        print(a[i][0], a[i][1])
