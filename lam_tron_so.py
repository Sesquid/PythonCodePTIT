t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    dem = 1; tmp = 0
    while(n // 10):
        tmp = (n % 10 + tmp) >= 5
        n //= 10
        dem *= 10
    print((n + tmp) * dem) 