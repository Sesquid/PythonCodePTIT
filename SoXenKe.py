def check(s):
    res = s[0]
    for i in range(0, len(s), 2):
        if res != s[i]:
            return False
    return True


t = int(input())

for i in range(t):
    n = input()
    if len(n) % 2 == 1 and n[0] != n[1] and check(n):
        print("YES")
    else: print("NO")
