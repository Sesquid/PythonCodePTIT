from itertools import permutations
t = int(input())
for i in range(t):
    n = int(input())
    a = [str(i) for i in range(1, n + 1)]
    perm = list(permutations(a))
    for i in perm:
        i = ''.join(list(i))
    perm.sort()
    perm.reverse()
    print(len(perm))
    for i in perm:
        for j in i:
            print(j, end='')
        print(end=' ')
    print()

