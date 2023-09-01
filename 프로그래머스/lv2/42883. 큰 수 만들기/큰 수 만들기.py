def solution(number, k):
    stack = []
    for n in number:
        if len(stack) == 0:
            stack.append(n)
        else:
            if stack[-1] < n and k != 0:
                while len(stack) >= 1 and stack[-1] < n:
                    stack.pop()
                    k -= 1
                    if k == 0:
                        break
                stack.append(n)
            else:
                stack.append(n)
    
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)