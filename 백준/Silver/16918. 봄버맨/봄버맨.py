import sys
input = sys.stdin.readline

def bomb(graph):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  bomb_graph = [['O' for _ in range(c)] for _ in range(r)]
  for i in range(r):
    for j in range(c):
      if graph[i][j] == 'O':
        bomb_graph[i][j] = '.'
        for k in range(4):
          nx, ny = i + dx[k], j + dy[k]
          if nx >= 0 and nx < r and ny >= 0 and ny < c:
            bomb_graph[nx][ny] = '.'
  return bomb_graph
    
r, c, n = map(int, input().split())
graph = []
for _ in range(r):
  graph.append(list(input().strip()))

if n == 1:
  for i in range(r):
    print(''.join(graph[i]))
elif n % 2 == 0:
  for i in range(r):
    print('O' * c)
elif n % 4 == 3:
  result = bomb(graph)
  for i in range(r):
    print(''.join(result[i]))
elif n % 4 == 1:
  tmp = bomb(graph)
  result = bomb(tmp)
  for i in range(r):
    print(''.join(result[i]))