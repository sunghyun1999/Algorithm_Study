def solution(s):
    answer = True
    stack = []
    for p in s:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                answer = False
    if len(stack) > 0:
        answer = False

    return answer