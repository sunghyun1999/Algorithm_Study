def solution(sequence, k):
    answer = []
    n = len(sequence)
    min_len = n + 1
    
    interval_sum = 0
    end = 0
    for start in range(n):
        while end < n and interval_sum < k:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k and end - start < min_len:
            min_len = end - start
            answer = [start, end-1]
        interval_sum -= sequence[start]
    
    return answer