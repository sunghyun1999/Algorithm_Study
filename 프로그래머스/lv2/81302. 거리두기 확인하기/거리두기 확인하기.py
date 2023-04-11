def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            if cell != 'P':
                continue
            
            if idx_row < 4:
                if place[idx_row+1][idx_col] == 'P': 
                    return 0
                if idx_row < 3:
                    if place[idx_row+2][idx_col] == 'P' and place[idx_row+1][idx_col] != 'X':
                        return 0
            if idx_col < 4:
                if place[idx_row][idx_col+1] == 'P':
                    return 0
                if idx_col < 3:
                    if place[idx_row][idx_col+2] == 'P' and place[idx_row][idx_col+1] != 'X':
                        return 0
            if idx_row < 4 and idx_col < 4:
                if place[idx_row+1][idx_col+1] == 'P' and (place[idx_row+1][idx_col] != 'X' or place[idx_row][idx_col+1] != 'X'):
                    return 0
            if idx_row < 4 and idx_col > 0:
                if place[idx_row+1][idx_col-1] == 'P' and (place[idx_row+1][idx_col] != 'X' or place[idx_row][idx_col-1] != 'X'):
                    return 0
    return 1

def solution(places):
    return [check(place) for place in places]