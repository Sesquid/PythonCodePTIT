t = int(input())
for i in range(t):
    s = input()
    flag = 1
    tmp = ord(s[-1]) - ord('0')
    for i in range(len(s) - 1):
        tmp += ord(s[i]) - ord('0')
        if abs(ord(s[i]) - ord(s[i + 1])) != 2:
            flag = 0
            break
    if tmp % 10 != 0:
        flag = 0
    print("YES" if flag == 1 else "NO")