from collections import defaultdict

def build_path(route, points):
    path = []
    cur_r, cur_c = points[route[0] - 1]
    path.append((cur_r, cur_c))
    
    for idx in route[1:]:
        tr, tc = points[idx - 1]
        while cur_r != tr or cur_c != tc:
            if cur_r != tr:
                cur_r += 1 if tr > cur_r else - 1
            else:
                cur_c += 1 if tc > cur_c else - 1
            path.append((cur_r, cur_c))
    return path

def solution(points, routes):
    answer = 0
    robot_paths = []
    max_time = 0
    
    for route in routes:
        path = build_path(route, points)
        robot_paths.append(path)
        max_time = max(max_time, len(path))
    
    for t in range(max_time):
        counter = defaultdict(int)
        for path in robot_paths:
            if t < len(path):
                counter[path[t]] += 1
                
        for v in counter.values():
            if v >= 2:
                answer += 1
    
    return answer