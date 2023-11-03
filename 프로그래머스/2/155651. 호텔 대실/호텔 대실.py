import heapq

def solution(book_time):
    book_time_ref = [(int(start[:2]) * 60 + int(start[3:]), int(end[:2]) * 60 + int(end[3:])) for start, end in book_time]
    book_time_ref.sort(key=lambda x: x[0])
    room = []
    for book in book_time_ref:
        if len(room) != 0 and room[0] <= book[0]:
            heapq.heappop(room)
        heapq.heappush(room, book[1]+10)
        
    return len(room)