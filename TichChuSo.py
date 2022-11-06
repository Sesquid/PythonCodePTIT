t = int(input())
for i in range(t):
    n = input()
    res = 1
    for j in n:
        res = res * int(j) if j != '0' else res
    print(res)