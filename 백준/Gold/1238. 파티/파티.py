import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))

def dijkstra(start, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur = heapq.heappop(pq)
        if cur_dist > dist[cur]:
            continue
        for nxt, cost in graph[cur]:
            new_dist = cur_dist + cost
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    return dist

dist_from_X = dijkstra(x, graph)
dist_to_X = dijkstra(x, reverse_graph)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, dist_from_X[i] + dist_to_X[i])

print(answer)
