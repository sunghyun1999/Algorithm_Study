import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")