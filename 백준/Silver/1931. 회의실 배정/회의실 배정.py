n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[1], x[0]))

res = 1
time = arr[0][1]
for i in range(1, n):
  if arr[i][0] >= time:
    res += 1
    time = arr[i][1]

print(res)