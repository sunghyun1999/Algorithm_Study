from math import lcm

def solution(signals):
    cycles = []
    
    for green, yellow, red in signals:
        cycles.append(green + yellow + red)
        
    period = 1
    
    for cycle in cycles:
        period = lcm(period, cycle)
        
    for t in range(1, period + 1):
        
        all_yellow = True
        
        for green, yellow, red in signals:
            cycle = green + yellow + red
            
            x = (t - 1) % cycle
            
            if not (green <= x < green + yellow):
                all_yellow = False
                break
        
        if all_yellow:
            return t
    
    return -1