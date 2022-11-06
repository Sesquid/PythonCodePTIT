t = int(input())
for i in range (t):
    n = int(input())
    print(1, end=' ')
    for i in range(2, n):
        if n % i == 0:
            cnt = 0;
            while n % i == 0:
                cnt += 1
                n /= i
            print(" * ", end = '')
            print(i, '^', cnt, sep='', end='')
    if n != 1:
        print(" * ", end='')
        print(n, '^', 1, sep='', end='')
    print()