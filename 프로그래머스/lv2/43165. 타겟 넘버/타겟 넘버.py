def solution(numbers, target):
    answer = 0
    def dfs(idx, res):
        nonlocal answer
        if idx == len(numbers):
            if res == target:
                answer += 1
            return
        else:
            dfs(idx+1, res+numbers[idx])
            dfs(idx+1, res-numbers[idx])
    
    dfs(0, 0)
    return answer