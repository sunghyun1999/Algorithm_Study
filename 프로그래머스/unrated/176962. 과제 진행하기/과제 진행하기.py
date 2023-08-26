def solution(plans):
    answer = []
    wating = []
    
    plans.sort(key=lambda x: x[1])
    for plan in plans:
        hour, minute = map(int, plan[1].split(":"))
        plan[1] = hour * 60 + minute
        plan[2] = int(plan[2])
        
    while plans:
        if len(plans) > 1:
            name1, start1, playtime1 = plans[0]
            name2, start2, playtime2 = plans[1]
            if start1 + playtime1 > start2:
                wating.append([name1, start1 + playtime1 - start2])
                plans.pop(0)
            else:
                answer.append(name1)
                plans.pop(0)
                interval = start2 - (start1 + playtime1)
                while wating:
                    if wating[-1][1] <= interval:
                        interval -= wating[-1][1]
                        answer.append(wating.pop()[0])
                    else:
                        wating[-1][1] -= interval
                        break
        else:
            answer.append(plans.pop()[0])
        
    while wating:
        answer.append(wating.pop()[0])
    
    return answer