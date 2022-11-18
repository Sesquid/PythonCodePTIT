def count(n):
    cnt = 0
    l = 1
    while l * (l + 1) < 2 * n:
        a = (n - l * (l + 1) / 2) / (l + 1)
        if a - int(a) == 0.0:
            cnt += 1
        l += 1
    return cnt

t = int(input()) 
for i in range (t):
    n = int(input())
    print(count(n))

