t = int(input())
for i in range(t):
    n = int(input())
    # cnt = 0;
    while n % 7 != 0:
        n += int(str(n)[::-1])
    print(n)