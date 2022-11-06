a = [0] * 100
a[1] = 1
a[2] = 1
for i in range(3, 93):
    a[i] = a[i - 1] + a[i - 2]

t = int (input())
for i in range(t):
    x, y = map(int, input().split())
    for i in range(x, y + 1):
        print(a[i], end=' ')
    print()


    
    