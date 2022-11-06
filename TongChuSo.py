def short(s):
    res = 0
    for i in s: res += ord(i) - ord('0')
    return str(res)

s = input()
res = 0
while len(s) > 1:
    s = short(s)
    res += 1
print(res)