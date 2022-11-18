t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    maxTMP = -1
    
    maxN = [0] * n
    for i in range(n):
        maxN[i] = maxTMP
        maxTMP = max(maxTMP, a[i])
    minN = [0] * n
    minTMP = 10 ** 11
    for i in range(n - 1, -1, -1):
        minN[i] = minTMP
        minTMP = min(minTMP, a[i])
    res = 0
    for i in range(n):
        if maxN[i] <= a[i] < minN[i]:
            res += 1
    print(res)
