import sys
import math
import heapq

input = sys.stdin.readline

n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]

visited = [False] * n
pq = []
heapq.heappush(pq, (0, 0))

total_cost = 0.0

while pq:
    cost, u = heapq.heappop(pq)

    if visited[u]:
        continue

    visited[u] = True
    total_cost += cost

    ux, uy = points[u]
    for v in range(n):
        if not visited[v]:
            vx, vy = points[v]
            dist = math.hypot(ux - vx, uy - vy)
            heapq.heappush(pq, (dist, v))

print(f"{total_cost:.2f}")
