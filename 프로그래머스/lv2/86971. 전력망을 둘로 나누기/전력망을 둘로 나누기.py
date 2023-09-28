from itertools import combinations
from collections import deque

def bfs(v, visited, graph):
    visited[v] = 1
    queue = deque([v])
    while queue:
        c = queue.popleft()
        for nv in graph[c]:
            if visited[nv] == 0:
                queue.append(nv)
                visited[nv] = 1

def solution(n, wires):
    answer = n-2
    for wire in combinations(wires, n-2):
        graph = [[] for _ in range(n+1)]
        visited = [0] * (n+1)
        visited[0] = -1
        for data in wire:
            graph[data[0]].append(data[1])
            graph[data[1]].append(data[0])
        bfs(1, visited, graph)
        answer = min(answer, abs(visited.count(1)-visited.count(0)))
    return answer