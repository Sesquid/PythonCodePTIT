t = int(input())
for i in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    l = min(a)
    r = max(a)
    print(r - l + 1 - len(a))