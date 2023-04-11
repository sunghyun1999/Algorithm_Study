def solution(line):
    answer = []
    pos = []
    n = len(line)
    x_max = y_max = -int(1e11)
    x_min = y_min = int(1e11)
    
    for i in range(n-1):
        a, b, e = line[i]
        for j in range(i+1, n):
            c, d, f = line[j]
            if a*d == b*c:
                continue
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])
                if x > x_max: x_max = x
                if y > y_max: y_max = y
                if x < x_min: x_min = x
                if y < y_min: y_min = y
                
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coordinate = [['.'] * x_len for _ in range(y_len)]
    
    for x, y in pos:
        nx = x + abs(x_min) if x_min < 0 else x - x_min
        ny = y + abs(y_min) if y_min < 0 else y - y_min
        coordinate[ny][nx] = '*'
        
    for result in coordinate:
        answer.append(''.join(result))
    
    return answer[::-1]