a = list()


def sinh(s):
    if len(s) >= 10:
        return
    if s.count('2') > len(s) / 2:
        a.append(int(s))
    sinh(s + '0')
    sinh(s + '1')
    sinh(s + '2')


sinh('1')
sinh('2')
a.sort()
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(n):
        print(a[i], end=' ')
    print()
