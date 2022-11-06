a = [0] * 1000001

def era():
    a[0] = a[1] = 1
    for i in range(2, 1001):
        if a[i] == 0:
            for j in range(i * i, 1000001, i):
                a[j] = 1

def rev(x):
    x = list(str(x))
    x.reverse()
    x = ''.join(x)
    return int(x)

era()

t = int(input())
for i in range(t):
    n = int(input())
    for i in range(13, n):
        if i < n and rev(i) < n and a[i] == 0 and a[rev(i)] == 0 and i < rev(i):
            print(i, rev(i), end=' ')
    print()