import sys
input = sys.stdin.readline

data1 = list(input().strip())
data2 = []
m = int(input())

for _ in range(m):
  command = input().split()
  if command[0] == 'L':
    if len(data1) != 0:
      data2.append(data1.pop())
  elif command[0] == 'D':
    if len(data2) != 0:
      data1.append(data2.pop())
  elif command[0] == 'B':
    if len(data1) != 0:
      data1.pop()
  elif command[0] == 'P':
    data1.append(command[1])

print(''.join(data1) + ''.join(list(reversed(data2))))