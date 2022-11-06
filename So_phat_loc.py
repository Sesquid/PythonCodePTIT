t = int(input())
for i in range(t):
    n = input()
    if len(n) < 2: print("NO")
    elif n[-1] == '6' and n[-2] == '8':
        print("YES")
    else:
        print("NO")
