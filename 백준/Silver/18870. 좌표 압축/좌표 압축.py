import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

compression = {}
for i, num in enumerate(sorted(list(set(data)))):
    compression[num] = i

for d in data:
    print(compression[d], end = ' ')
