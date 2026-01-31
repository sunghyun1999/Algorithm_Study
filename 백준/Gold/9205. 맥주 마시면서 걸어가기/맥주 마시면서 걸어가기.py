from collections import deque
import sys
input = sys.stdin.readline

def can_go(home, stores,festival):
    queue = deque([home])
    visited = [False] * len(stores)

    while queue:
        x, y = queue.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            return 'happy'

        for i in range(len(stores)):
            if not visited[i]:
                sx, sy = stores[i]
                if abs(x - sx) + abs(y - sy) <= 1000:
                    visited[i] = True
                    queue.append((sx, sy))

    return 'sad'

t = int(input())

for _ in range(t):
    n = int(input())

    points = [tuple(map(int, input().split())) for _ in range(n + 2)]

    home = points[0]
    stores = points[1:-1]
    festival = points[-1]

    print(can_go(home, stores, festival))
