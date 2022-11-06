t = int(input())
for i in range(t):
    x = int(input())
    y = int(input())
    while x != 0:
        tmp = y % x
        y = x
        x = tmp
    print(y)
