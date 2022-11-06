import math

l, r = map(int, input().split())
for i in range (l, r):
    for j in range(i + 1, r):
        if math.gcd(i, j) == 1:
            for k in range(j + 1, r + 1):
                if math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                    print('(', end = '')
                    print(i,',', end=' ', sep='')
                    print(j, ',', end=' ', sep='')
                    print(k, end='')
                    print(')')
