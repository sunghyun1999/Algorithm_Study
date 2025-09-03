n = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
    row, col = map(int, input().split())
    board[row][col] = 1

direction_changes = []
for _ in range(int(input())):
    t, c = input().split()
    direction_changes.append((int(t), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    return (direction - 1 + 4) % 4 if c == 'L' else (direction + 1) % 4

direction = 0
time = 0
x, y = 1, 1
snake = [(x, y)]
turn_idx = 0

while True:
    nx, ny = x + dx[direction], y + dy[direction]

    if not (1 <= nx <= n and 1 <= ny <= n) or board[nx][ny] == 2:
        time += 1
        break

    if board[nx][ny] == 0:
        px, py = snake.pop(0)
        board[px][py] = 0

    board[nx][ny] = 2
    snake.append((nx, ny))

    x, y = nx, ny
    time += 1

    if turn_idx < len(direction_changes) and direction_changes[turn_idx][0] == time:
        direction = turn(direction, direction_changes[turn_idx][1])
        turn_idx += 1

print(time)
