n, k = map(int, input().split())
a = [[int(i)] for i in input().split()]
b = [[int(i)] for i in input().split()]
for i in range(n):
    a[i] += b[i]
a = sorted(a, key=lambda x: x[0] - x[1])
# print(a)
sum = 0
for i in range(k):
    sum += a[i][0]
for i in range(k, n):
    sum += a[i][1] if a[i][1] < a[i][0] else a[i][0]
print(sum)

