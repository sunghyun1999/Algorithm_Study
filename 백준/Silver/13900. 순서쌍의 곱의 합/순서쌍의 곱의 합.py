from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

total_sum = sum(nums)
res = 0

for num in nums:
    total_sum -= num
    res += num * total_sum

print(res)
