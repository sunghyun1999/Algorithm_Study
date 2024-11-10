def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        while stack and prices[i] <= prices[stack[-1]]:
            stack.pop()
            
        if stack:
            answer[i] = stack[-1] - i
        else:
            answer[i] = n - i - 1
        
        stack.append(i)
    
    return answer