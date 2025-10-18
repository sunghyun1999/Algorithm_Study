import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1)
distance[K] = 0
queue = [(0, K)]

while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for v, w in graph[now]:
        if distance[v] > dist + w:
            distance[v] = dist + w
            heapq.heappush(queue, (distance[v], v))

for i in range(1, V + 1):
    print(distance[i] if distance[i] != INF else 'INF')
