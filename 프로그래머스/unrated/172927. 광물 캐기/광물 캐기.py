def solution(picks, minerals):
    answer = 0
    minerals = minerals[:sum(picks)*5]
    groups = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    
    costs = []
    for group in groups:
        cost = [0, 0, 0]
        for mineral in group:
            if mineral == "diamond":
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mineral == "iron":
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            elif mineral == "stone":
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)
        
    costs.sort(key = lambda x: -sum(x))
    for cost in costs:
        if picks[0] > 0:
            answer += cost[0]
            picks[0] -= 1
            continue
        elif picks[1] > 0:
            answer += cost[1]
            picks[1] -= 1
            continue
        elif picks[2] > 0:
            answer += cost[2]
            picks[2] -= 1
            continue
    
    return answer