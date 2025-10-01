import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = {}
    
    for idx, op in enumerate(operations):
        cmd, val = op.split()
        val = int(val)
        
        if cmd == 'I':
            heapq.heappush(min_heap, (val, idx))
            heapq.heappush(max_heap, (-val, idx))
            visited[idx] = True
        else:
            if val == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]