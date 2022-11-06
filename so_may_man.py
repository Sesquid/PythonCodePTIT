str = input()
res = 0
for i in range (0, len(str)):
    res += 1 if str[i] == '4' or str[i] == '7' else 0
# print(res)
print("YES" if res == 4 or res == 7 else "NO")