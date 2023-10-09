import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

space = [[0] * w for _ in range(h)]
for j in range(w):
  for i in range(block[j]):
    space[i][j] = 1

answer = 0
for i in range(h):
  for j in range(1, w-1):
    if space[i][j] == 0:
      left = -1
      right = w
      for k in range(j-1, -1, -1):
        if space[i][k] == 1:
          left = k
          break
      for k in range(j+1, w):
        if space[i][k] == 1:
          right = k
          break
      if left != -1 and right != w:
        answer += 1

print(answer)