from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

fire_time = [[-1] * c for _ in range(r)]
jihun_time = [[-1] * c for _ in range(r)]

fire_q = deque()
jihun_q = deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            fire_q.append((i, j))
            fire_time[i][j] = 0
        if maze[i][j] == 'J':
            jihun_q.append((i, j))
            jihun_time[i][j] = 0

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while fire_q:
    x, y = fire_q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if maze[nx][ny] != '#' and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_q.append((nx, ny))

while jihun_q:
    x, y = jihun_q.popleft()

    if x == 0 or x == r - 1 or y == 0 or y == c - 1:
        print(jihun_time[x][y] + 1)
        exit()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < r and 0 <= ny < c):
            continue
        if maze[nx][ny] == '#':
            continue
        if jihun_time[nx][ny] != -1:
            continue

        next_time = jihun_time[x][y] + 1

        if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= next_time:
            continue

        jihun_time[nx][ny] = next_time
        jihun_q.append((nx, ny))

print("IMPOSSIBLE")
