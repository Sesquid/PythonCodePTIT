n = int(input())
a = list(map(float, input().split()))
a.sort()
# print(a)
Max = a[0]
Min = a[len(a) - 1]
res = 0
cnt = 0

for i in a:
    if i != Min and i != Max:
        cnt += 1
        res += i
res /= cnt
print("{:.2f}".format(res))
