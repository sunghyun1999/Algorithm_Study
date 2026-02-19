import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

avg = sum(nums) / n
mean = int(avg + 0.5) if avg >= 0 else int(avg - 0.5)
print(mean)

print(nums[n // 2])

counter = Counter(nums)
max_freq = max(counter.values())
modes = [num for num, freq in counter.items() if freq == max_freq]
modes.sort()

print(modes[0] if len(modes) == 1 else modes[1])

print(nums[-1] - nums[0])
