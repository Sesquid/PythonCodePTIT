t = int(input())
for i in range(t):
    s = input()
    flag = 1
    for i in range (len(s)):
        if s[i] != '0' and s[i] != '1' and s[i] != '2':
            flag = 0
            break
    print("YES" if flag == 1 else "NO")