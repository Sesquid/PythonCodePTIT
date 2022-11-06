t = int(input())
for i in range(t):
    x, y = input().split()
    if x > y: x, y = y, x
    l = []
    while len(l) != 2:
        tmp = input().split()
        l += tmp

    a, b = l[0], l[1]

    a1 = int(a.replace(x, y))
    b1 = int(b.replace(x, y))
    a2 = int(a.replace(y, x))
    b2 = int(b.replace(y, x))

    print(a2 + b2, a1 + b1)