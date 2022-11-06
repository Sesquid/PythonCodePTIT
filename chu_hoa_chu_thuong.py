
dem = 0
s = input()
for i in range(0, len(s)):
    dem += 1 if s[i].islower() else -1
print(s.lower() if dem >= 0 else s.upper())