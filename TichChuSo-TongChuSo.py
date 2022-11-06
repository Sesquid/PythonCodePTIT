t = int(input())

# def check(n):
#     for i in range(1, len(n), 2):
#         if n[i] != '0': return True
#     return False

for i in range(t):
    n = input()
    tong = 0
    tich = 1
    for i in range(0, len(n)):
        if i % 2 == 1:
            tong += int(n[i])
        elif int(n[i]) != 0: tich *= int(n[i])
    # if not check(n): tich = 0
    print(tich, tong, sep=' ')