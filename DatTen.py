from itertools import combinations

n, k = map(int, input().split())
s = list(set(list(input().split())))
s.sort()
com = combinations(s, k)
for i in list(com):
    for j in range(k):
        print(i[j], end=' ')
    print()