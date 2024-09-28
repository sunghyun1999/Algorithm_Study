def solution(dirs):
    answer = 0
    x, y = 0, 0
    udrl = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    roads = set()
    
    for d in dirs:
        dx, dy = udrl[d]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            roads.add(((x, y), (nx, ny)))
            roads.add(((nx, ny), (x, y)))
            x = nx
            y = ny
        
    return len(roads) // 2