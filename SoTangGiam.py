t = int(input())
for i in range (t):
    s = input()
    mL = list(s).index(max(list(s)))
    flag = 1
    for i in range (len(s) - 1):
        if i >= mL:
            if s[i] <= s[i + 1]:
                flag = 0
                break
        else:
            if s[i] >= s[i + 1]:
                flag = 0
                break
    print("NO" if flag == 0 or len(s) < 3 else "YES")