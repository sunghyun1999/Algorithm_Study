t = int(input())

for _ in range(t):
    data = input()
    stack = []
    valid = True
    for ch in data:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                valid = False
                break
    if valid and not stack:
        print('YES')
    else:
        print('NO')
