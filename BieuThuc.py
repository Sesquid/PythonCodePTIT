

t = int(input())
for i in range(t):
    s = input()
    open = 1
    d = []
    for i in s:
        if i == '(':
            print(open, end=' ')

            d.append(open)
            open += 1
        elif i == ')':
            print(d[-1], end=' ')
            d.pop()
    print()
