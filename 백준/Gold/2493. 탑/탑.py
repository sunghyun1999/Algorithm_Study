import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
  while stack:
    if stack[-1][1] > tower[i]:
      answer.append(stack[-1][0]+1)
      break
    else:
      stack.pop()
  if len(stack) == 0:
    answer.append(0)
  stack.append((i, tower[i]))

print(' '.join(map(str, answer)))