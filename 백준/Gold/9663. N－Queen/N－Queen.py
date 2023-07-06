def promising(graph, row, col):
  for i in range(1, row):
    if graph[i] == col or abs(graph[i]-col) == row-i:
      return False
  return True

def nqueen(graph, row, num):
  global result
  if row == num + 1:
    result += 1
    return
  for col in range(1, num+1):
    if promising(graph, row, col):
      graph[row] = col
      nqueen(graph, row+1, num)

n = int(input())
graph = [0 for _ in range(n+1)]
visited = [False] * (n+1)

result = 0
nqueen(graph, 1, n)
print(result)