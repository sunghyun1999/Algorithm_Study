s = input()
a_cnt = s.count('a')
s += s[:a_cnt-1]

interval = s[:a_cnt]
answer = interval.count('b')
for i in range(a_cnt, len(s)):
  interval = interval[1:] + s[i]
  answer = min(answer, interval.count('b'))

print(answer)