import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

prefix_sum = 0
answer = 0

for x in arr:
    answer += x * prefix_sum
    prefix_sum += x

print(answer)
