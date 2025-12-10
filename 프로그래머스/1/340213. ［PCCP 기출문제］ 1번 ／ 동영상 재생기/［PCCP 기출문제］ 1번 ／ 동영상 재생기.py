def to_sec(time_str):
    mm, ss = map(int, time_str.split(":"))
    return mm * 60 + ss

def to_mmss(sec):
    mm = sec // 60
    ss = sec % 60
    return f"{mm:02d}:{ss:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    if op_start <= pos <= op_end:
        pos = op_end

    for cmd in commands:
        if cmd == "prev":
            pos = max(0, pos - 10)
        elif cmd == "next":
            pos = min(video_len, pos + 10)

        if op_start <= pos <= op_end:
            pos = op_end

    return to_mmss(pos)
    