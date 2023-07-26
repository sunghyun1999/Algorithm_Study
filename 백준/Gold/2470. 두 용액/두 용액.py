n = int(input())
arr = list(map(int, input().split()))

arr.sort()
start, end = 0, n-1

mix_value = abs(arr[start] + arr[end])
ans = [arr[start], arr[end]]

while start < end:
  tmp = arr[start] + arr[end]
  if abs(tmp) < mix_value:
    mix_value = abs(tmp)
    ans = [arr[start], arr[end]]
    if mix_value == 0:
      break
  if tmp < 0:
    start += 1
  else:
    end -= 1

print(ans[0], ans[1])