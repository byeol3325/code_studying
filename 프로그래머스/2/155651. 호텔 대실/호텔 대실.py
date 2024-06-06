import heapq as hq

def can_next_time(a: str, b: str) -> int:
    """
    check next book_time (end_time + 10 min <= next start_time)
    
    Params
        a : end time of book time
        b : start time of book time
    
    Returns
        bool : if can do next time, return 1. else, return 0.
    
    """
    a = a.split(':'); a_minute = 60 * int(a[0]) + int(a[1])
    b = b.split(':'); b_minute = 60 * int(b[0]) + int(b[1])
    
    if a_minute + 10 <= b_minute:
        return 1
    return 0

def solution(book_time: list) -> int:
    rooms = [] # save end time
    book_time = sorted(book_time)#, key = lambda x: (x[1], x[0])) # sort book time by end time
    
    for start, end in book_time:
        # if no room or need to more room
        if len(rooms) == 0 or can_next_time(rooms[0], start) == 0:
            hq.heappush(rooms, end)
        elif can_next_time(rooms[0], start) == 1:
            hq.heappop(rooms)
            hq.heappush(rooms, end)
    
    return len(rooms)