from itertools import permutations
s = list(input())
s = list(permutations(s))
for i in s:
    for j in i:
        print(j, end='')
    print()
