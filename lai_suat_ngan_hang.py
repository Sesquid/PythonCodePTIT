t = int(input())
while t > 0:
    t -= 1
    a, b, c = map(float, input().split(" "))
    res = 0
    while a < c:
        a *= (1 + b * 0.01)
        res += 1
    # print(a, b, c)
    print(res)