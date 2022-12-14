n = int(input())
a = ['{:0b}'.format(int(u)) for u in input().split()]
for i in range(n):
    flag = 0
    u = a[i]
    # for i in range(len(u)):
    if(u.count("01") + u.count("10") <= 1):
        # print(u)
        flag = 1
        # u = u[-1] + u[:-1]
        
    print(1 if flag else 0, end=' ')
