t = int(input())
for i in range(t):
    n = int(input())
    l = 1 if n % 2 == 1 else 2
    res = 0.0
    for i in range(l, n + 1, 2):
        res += 1 / i
        # print(res)
    print('{:.6f}'.format(res))