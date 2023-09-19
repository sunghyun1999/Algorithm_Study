s = list(input())
half_x = s.count('1') // 2
half_y = s.count('0') // 2

cnt_x = 0
cnt_y = 0
for i in range(len(s)):
  if s[i] == '1' and half_x != cnt_x:
    s[i] = ''
    cnt_x += 1
  if s[len(s)-i-1] == '0' and half_y != cnt_y:
    s[len(s)-i-1] = ''
    cnt_y += 1

print(''.join(s))