def solution(d, budget):
    answer = 0
    d.sort()
    for amount in d:
        if amount <= budget:
            answer += 1
            budget -= amount
        else:
            break
    
    return answer