ke = {}
used = set()
def DFS(node, ke, used):
    if node not in used:
        used.add(node)
        for neighbor in ke[node]:
            DFS(neighbor, ke, used)

n, m, x = map(int, input().split())
for i in range(1, n + 1):
    ke[i] = []
for i in range(m):
    u, v = map(int, input().split())
    ke[u].append(v)
    ke[v].append(u)
flag = 0
DFS(x, ke, used)
for i in range(1, n + 1):
    if not i in used:
        flag = 1
        print(i)
if flag == 0:
    print(0)