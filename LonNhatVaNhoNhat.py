while True:
    n = int(input())
    if n == 0: break
    minN = 10 ** 100
    maxN = -1
    for i in range(n):
        tmp = int(input())
        minN = min(minN, tmp)
        maxN = max(maxN, tmp)
    print("BANG NHAU" if minN == maxN else '{} {}'.format(minN, maxN), sep=' ')
