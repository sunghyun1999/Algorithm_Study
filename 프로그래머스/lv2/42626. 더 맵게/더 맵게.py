import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        second = heapq.heappop(scoville)
        mixed = first + second * 2
        answer += 1
        heapq.heappush(scoville, mixed)
    
    return answer