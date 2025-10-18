def solution(sequence, k):
    n = len(sequence)
    answer = [0, n - 1]
    min_len = n + 1
    
    start = 0
    end = 0
    interval_sum = 0
    
    while end < n:
        interval_sum += sequence[end]
        end += 1
        
        while interval_sum > k:
            interval_sum -= sequence[start]
            start += 1
            
        if interval_sum == k and (end - start) < min_len:
            answer = [start, end - 1]
            min_len = end - start
    
    return answer