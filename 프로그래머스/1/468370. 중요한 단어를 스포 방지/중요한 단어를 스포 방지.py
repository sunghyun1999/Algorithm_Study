def solution(message, spoiler_ranges):
    words = []
    
    i = 0
    n = len(message)
    
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        
        start = i
        
        while i < n and message[i] != ' ':
            i += 1
            
        end = i - 1
        
        word = message[start:end + 1]
        
        words.append((word, start, end))
        
    spoiler_words = set()
    normal_words = set()
    
    for word, start, end in words:
        
        is_spoiler = False
        
        for s, e in spoiler_ranges:
            if start <= e and s <= end:
                is_spoiler = True
                break
            
            if start > e:
                continue
        
        if is_spoiler:
            spoiler_words.add(word)
        else:
            normal_words.add(word)
    
    answer = spoiler_words - normal_words
    
    return len(answer)