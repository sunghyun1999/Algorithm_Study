from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])

cnt = 0
while True:
  if len(queue) == 1:
    print(queue.popleft())
    break
  if cnt % 2 == 0:
    queue.popleft()
  if cnt % 2 == 1:
    queue.append(queue.popleft())
  cnt += 1
