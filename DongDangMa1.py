n, M = map(int, input().split())
for i in range(n):
    flag = 0
    u, v = map(int, input().split())
    u = '{:0b}'.format(u).zfill(M)
    v = '{:0b}'.format(v).zfill(M)
    l = set()
    for i in range(M):
        u = u[-1] + u[:-1]
        l.add(u)
    if v in l: 
        flag = 1
    print(1 if flag else 0)
    