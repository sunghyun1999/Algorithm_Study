import heapq

def solution(jobs):
    answer = []
    waiting = []
    jobs.sort()
    now = 0
    num = len(jobs)
    while len(answer) != num:
        while jobs and jobs[0][0] <= now:
            job = jobs.pop(0)
            heapq.heappush(waiting, (job[1], job[0]))
        if jobs and len(waiting) == 0:
            job = jobs.pop(0)
            now = job[0]
            heapq.heappush(waiting, (job[1], job[0]))
        completion, arrival = heapq.heappop(waiting)
        now += completion
        answer.append(now-arrival)
    
    return sum(answer) // num