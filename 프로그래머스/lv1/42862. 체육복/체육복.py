def solution(n, lost, reserve):
    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))
    set_lost.sort()
    answer = n - len(set_lost)
    for l in set_lost:
        if l-1 in set_reserve:
            set_reserve.remove(l-1)
            answer += 1
        elif l+1 in set_reserve:
            set_reserve.remove(l+1)
            answer += 1
    
    return answer