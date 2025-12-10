def solution(video_len, pos, op_start, op_end, commands):
    video_min, video_sec = map(int, video_len.split(':'))
    pos_min, pos_sec = map(int, pos.split(':'))
    op_start_min, op_start_sec = map(int, op_start.split(':'))
    op_end_min, op_end_sec = map(int, op_end.split(':'))
    
    video_total_sec = video_min * 60 + video_sec
    pos_total_sec = pos_min * 60 + pos_sec
    op_start_total_sec = op_start_min * 60 + op_start_sec
    op_end_total_sec = op_end_min * 60 + op_end_sec
    
    curr = op_end_total_sec if op_start_total_sec <= pos_total_sec <= op_end_total_sec else pos_total_sec
    for cmd in commands:
        if cmd == 'prev':
            if curr < 10:
                curr = 0
            else:
                curr -= 10
        elif cmd == 'next':
            if video_total_sec - curr < 10:
                curr = video_total_sec
            else:
                curr += 10
        
        if op_start_total_sec <= curr <= op_end_total_sec:
            curr = op_end_total_sec
            
    ans_min, ans_sec = curr // 60, curr % 60
    
    return f"{ans_min:02d}" + ':' + f"{ans_sec:02d}"