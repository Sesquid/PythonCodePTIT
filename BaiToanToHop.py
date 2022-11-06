from itertools import combinations

n, k = map(int, input().split())
s = list(set(map(int, input().split())))
s.sort()
s = list(combinations(s, k))
# print(s)
for i in s:
    for j in i:
        print(j, end=' ')
    print()