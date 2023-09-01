def solution(name):
    up_down = []
    for alpha in name:
        up_down.append(min(ord(alpha)-ord('A'), ord('Z')-ord(alpha)+1))
    
    min_move = len(name)
    for i in range(len(name)):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, i*2 + len(name)-next, i + 2*(len(name)-next))
    
    return sum(up_down) + min_move   