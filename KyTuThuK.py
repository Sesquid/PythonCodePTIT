def find(n, k):
    if k == 2 ** (n - 1):
        return chr(n + ord('A') - 1)
    k %= (2 ** (n - 1))
    return find(n - 1, k)


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(find(n, k))

