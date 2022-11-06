t = int(input())
for i in range (t):
    n = input()
    flag = True
    for i in range(0, len(n) - 1):
        if n[i] > n[i + 1]:
            flag = False
            break
    print("YES" if flag == True else "NO")

