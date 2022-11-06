import re

n = int(input())
a = []
d = {}
for i in range(n):
    s = input().lower()
    s = re.split('[^\\w\\d]', s)
    a += s
# print(a)
for i in a:
    i = ''.join([x for x in i if not x.isdigit()])
    if i != '':
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
a = [[i, d[i] ] for i in d]
a = sorted(a, key=lambda x: (-x[1], x[0]))
for i in range( len(a)):
    print(a[i][0], a[i][1])
