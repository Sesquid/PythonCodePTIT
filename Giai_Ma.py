t = int(input())
for i in range (t):
    s = input()
    for i in range(0, len(s), 2):
        print(s[i] * int(s[i + 1]), end='')
    print()
