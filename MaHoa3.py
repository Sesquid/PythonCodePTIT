a ="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate(s):
    global a
    res = 0
    ans = ""
    for i in s:
        res += (ord(i) - ord('A'))
    for i in range(len(s)):
        ans += a[ord(s[i]) - ord('A') + (res % 26)]
    return ans
def rotate2(x, y):
    ans = ""
    for i in range(len(y)):
        ans += a[(ord(x[i]) - ord('A') + ord(y[i]) - ord('A')) % 26]
    return ans
t = int(input())
for i in range(t):
    s = input()
    s1 = rotate(s[:(len(s) // 2)])
    s2 = rotate(s[(len(s) // 2):])
    s1 = rotate2(s1, s2)
    print(s1)

