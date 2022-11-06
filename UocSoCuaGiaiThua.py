t = int(input())

for i in range(t):

    n, p = map(int, input().split())
    res = 0

    for x in range(2, n + 1):
        j = x
        while j % p == 0:
            # print(j)
            j = j // p
            res += 1
    print(res)