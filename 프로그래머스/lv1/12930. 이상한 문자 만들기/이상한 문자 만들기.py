def solution(s):
    answer = list(s)
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == ' ':
            cnt = 0
            continue
        answer[i] = answer[i].upper() if cnt % 2 == 0 else answer[i].lower()
        cnt += 1
        
    return ''.join(answer)