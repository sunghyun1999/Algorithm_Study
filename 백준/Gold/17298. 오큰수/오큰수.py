import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [-1] * n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(map(str, ans)))
