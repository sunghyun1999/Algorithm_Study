import sys
input = sys.stdin.readline

n = int(input())
balls = list(input().strip())

red_cnt = balls.count('R')
blue_cnt = balls.count('B')

answer = min(red_cnt, blue_cnt)

cnt = 0
for i in range(n):
  if balls[i] == balls[0]:
    cnt += 1
  else:
    break

if balls[0] == 'R':
  answer = min(answer, red_cnt-cnt)
else:
  answer = min(answer, blue_cnt-cnt)

reverse_cnt = 0
for i in range(n-1, -1, -1):
  if balls[i] == balls[n-1]:
    reverse_cnt += 1
  else:
    break
    
if balls[-1] == 'R':
  answer = min(answer, red_cnt-reverse_cnt)
else:
  answer = min(answer, blue_cnt-reverse_cnt)

print(answer)