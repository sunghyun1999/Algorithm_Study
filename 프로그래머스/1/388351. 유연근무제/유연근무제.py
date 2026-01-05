def to_minutes(t):
    return (t // 100) * 60 + (t % 100)

def solution(schedules, timelogs, startday):
    answer = len(schedules)
    
    for i in range(len(schedules)):
        base = to_minutes(schedules[i])
        for j in range(7):
            day = (startday + j - 1) % 7 + 1
            
            if day >= 6:
                continue
                
            actual = to_minutes(timelogs[i][j])
            if actual - base > 10:
                answer -= 1
                break
    
    return answer