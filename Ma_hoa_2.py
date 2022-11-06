P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    ip = input()
    if ip == "0": break
    k, s = ip.split()
    k = int(k)
    # print(k)
    if k == 0: break;
    n = ""
    for i in s:
        n = P[(P.index(i) + k) % 28] + n
    print(n)