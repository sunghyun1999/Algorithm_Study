import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(input())

result = ''
hamming = 0

for i in range(m):
  count = [0, 0, 0, 0] # A, C, G, T
  for j in range(n):
    if arr[j][i] == 'A':
      count[0] += 1
    elif arr[j][i] == 'C':
      count[1] += 1
    elif arr[j][i] == 'G':
      count[2] += 1
    elif arr[j][i] == 'T':
      count[3] += 1
  idx = count.index(max(count))
  if idx == 0:
    result += 'A'
  elif idx == 1:
    result += 'C'
  elif idx == 2:
    result += 'G'
  elif idx == 3:
    result += 'T'
  hamming += n - max(count)

print(result)
print(hamming)