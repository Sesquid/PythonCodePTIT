n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 10
ansN = 0
for i in range(n - 1, -1, -1):
    res = 0
    for j in range(n):
        res += abs(a[i] - a[j])
    if res <= ans:
        ans = res
        ansN = a[i]
print(ans, ansN)