import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))

start = 0
end = n-1

a = solution[0]
b = solution[-1]

min_value = float('inf')

while start < end:
  tmp = solution[start] + solution[end]
  if tmp == 0:
    a = solution[start]
    b = solution[end]
    break
  elif abs(tmp) < min_value:
    min_value = abs(tmp)
    a = solution[start]
    b = solution[end]
  if tmp > 0:
    end -= 1
  else:
    start += 1

print(a, b)