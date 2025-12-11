def puzzle(diff, time_cur, time_prev, level):
    if diff <= level:
        return time_cur
    else:
        return (diff - level) * (time_cur + time_prev) + time_cur

def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in range(len(diffs)):
            time_prev = times[i-1] if i > 0 else 0
            total += puzzle(diffs[i], times[i], time_prev, mid)
        
        if total <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer