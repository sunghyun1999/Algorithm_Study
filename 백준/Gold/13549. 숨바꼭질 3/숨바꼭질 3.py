import heapq
MAX = 100001
INF = int(1e9)

def dijkstra(x):
  q = []
  heapq.heappush(q, (0, x))
  distance[x] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in [(now-1, dist+1), (now+1, dist+1), (now*2, dist)]:
      if 0 <= i[0] <= 100000 and i[1] < distance[i[0]]:
        distance[i[0]] = i[1]
        heapq.heappush(q, (i[1], i[0]))

n, k = map(int, input().split())
distance = [INF] * MAX
dijkstra(n)

print(distance[k])