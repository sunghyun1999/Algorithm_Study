import sys
input = sys.stdin.readline

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True

N = int(input().strip())
M = int(input().strip())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    edges.append((c, a, b))

edges.sort()

parent = list(range(N+1))
total = 0
cnt = 0

for cost, a, b in edges:
    if union(parent, a, b):
        total += cost
        cnt += 1
        if cnt == N - 1:
            break

print(total)
