import math


def nC2(n):
    f = math.factorial
    return f(n) // f(2) // f(n - 2)

a = []
res = 0
n = int(input())
for i in range(n):
    s = input()
    res += nC2(s.count('C'))
    a.append(s)
for j in range(n):
    tmp = 0
    for i in range(n):
        if a[i][j] == 'C': tmp += 1
    if tmp >= 2: res += nC2(tmp)
print(res)
