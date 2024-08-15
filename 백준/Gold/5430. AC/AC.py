import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p = input()
  n = int(input())
  data = input().strip()
  
  data = [] if n == 0 else list(map(int, data[1:-1].split(',')))
  
  is_error = False
  reverse = False
  x, y = 0, n
  for i in range(len(p)):
    if p[i] == 'R':
      reverse = not reverse
    elif p[i] == 'D':
      if x < y:
        if reverse:
          y -= 1
        else:
          x += 1
      else:
        is_error = True
        break

  if is_error:
    print('error')
  else:
    data = data[x:y]
    if reverse:
      data.reverse()
    print('[' + ','.join(map(str, data)) + ']')
