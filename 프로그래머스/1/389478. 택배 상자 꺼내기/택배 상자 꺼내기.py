def solution(n, w, num):
    answer = 0
    
    layer = (num - 1) // w
    pos_in_layer = (num - 1) % w
    
    if layer % 2 == 1:
        pos_in_layer = w - pos_in_layer - 1
        
    top_layer = (n - 1) // w
    pos_in_top_layer = (n - 1) % w
    if top_layer % 2 == 1:
        pos_in_top_layer = w - pos_in_top_layer - 1
        if pos_in_layer < pos_in_top_layer:
            top_layer -= 1
    else:
        if pos_in_layer > pos_in_top_layer:
            top_layer -= 1
    
    return top_layer - layer + 1