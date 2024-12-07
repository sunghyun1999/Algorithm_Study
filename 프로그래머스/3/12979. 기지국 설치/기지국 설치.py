import math

def solution(n, stations, w):
    answer = 0
    range = 2 * w + 1
    start = 1
    for s in stations:
        if s - w - start > 0:
            answer += math.ceil((s -w-start) / range)
        start = s + w + 1
    if n - start + 1 > 0:
        answer += math.ceil((n-start+1) / range)
            
    return answer