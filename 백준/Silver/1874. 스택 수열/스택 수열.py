import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []

next_num = 1

for num in sequence:
    while next_num <= num:
        stack.append(next_num)
        result.append('+')
        next_num += 1

    if stack and stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit(0)

print('\n'.join(result))
