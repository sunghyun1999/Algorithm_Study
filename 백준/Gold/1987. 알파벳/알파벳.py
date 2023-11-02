import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0 ,0, -1, 1]

def dfs(cnt, x, y):
  global answer
  answer = max(answer, cnt)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < r and ny >= 0 and ny < c:
      if visited[board[nx][ny]] == 0: 
        visited[board[nx][ny]] = 1
        dfs(cnt+1, nx, ny)
        visited[board[nx][ny]] = 0

r, c = map(int, input().split())
board = []
for _ in range(r):
  board.append(list(map(lambda x: ord(x)-65, input().rstrip())))

visited = [0] * 26
visited[board[0][0]] = 1

answer = 0
dfs(1, 0, 0)
print(answer)