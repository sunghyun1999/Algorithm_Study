import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(idx, val, add, sub, mul, div):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return

    if add > 0:
        dfs(idx + 1, val + nums[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, val - nums[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, val * nums[idx], add, sub, mul - 1, div)
    if div > 0:
        if val < 0:
            dfs(idx + 1, -(-val // nums[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, val // nums[idx], add, sub, mul, div - 1)

dfs(1, nums[0], add, sub, mul, div)

print(max_val)
print(min_val)
