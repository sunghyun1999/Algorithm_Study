n = int(input())
arr = list(map(int ,input().split()))

def men(num):
  for i in range(num, n+1, num):
    arr[i-1] = 1 - arr[i-1]

def women(num):
  arr[num-1] = 1 - arr[num-1]
  left, right = num-1, num+1
  while True:
    if left >= 1 and left <= n and right >= 1 and right <= n:
      if arr[left-1] == arr[right-1]:
        arr[left-1] = 1 - arr[left-1]
        arr[right-1] = 1 - arr[right-1]
        left -= 1
        right += 1
      else:
        break
    else:
      break

student_num = int(input())
for i in range(student_num):
  gender, num = map(int, input().split())
  if gender == 1:
    men(num)
  elif gender == 2:
    women(num)

for i in range(1, n+1):
  print(arr[i-1], end=' ')
  if i % 20 == 0:
    print()