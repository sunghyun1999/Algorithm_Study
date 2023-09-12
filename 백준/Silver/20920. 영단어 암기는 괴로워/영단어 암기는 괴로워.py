import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = {}
for _ in range(n):
  word = input().strip()
  if len(word) < m:
    continue
  if word in words.keys():
    words[word][0] += 1
  else:
    words[word] = [1, len(word), word]

arr = sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))
for data in arr:
  print(data[0])