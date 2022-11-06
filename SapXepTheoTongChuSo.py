import functools


def cnt(n):
    n = str(n)
    res = 0
    for i in n:
        res += int(i)
    return res

def cmp(a, b):
    if cnt(a) == cnt(b): return a - b
    return cnt(a) - cnt(b)

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, key=functools.cmp_to_key(cmp))
    for i in a:
        print(i, end=' ')
    print()
