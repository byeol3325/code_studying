from collections import deque

def solution(arr):
    answer = [0, 0] # [0의 수, 1의 수]
    # 0 ~ 3 => 01 / 23
    
    def do_next(loc: list, size: int):
        """
        loc : arr에서 위치.
        size : 한 변 길이
        """
        if size == 1:
            answer[arr[loc[0]][loc[1]]] += 1
            return 0
        
        value = arr[loc[0]][loc[1]]
        for i in range(size):
            for j in range(size):
                if arr[loc[0]+i][loc[1]+j] != value:
                    return 1
        
        answer[value] += 1
        return 0
    
    waiting_list = deque() # [loc, size]
    waiting_list.append([[0,0],len(arr)])
    while True:
        next_waiting = deque()
        for i in range(len(waiting_list)):
            loc, size = waiting_list.pop()
            next_ = do_next(loc, size)
            if next_ == 0:
                continue
            else:
                next_waiting.append([loc, size//2])
                next_waiting.append([[loc[0]+size//2, loc[1]],         size//2])
                next_waiting.append([[loc[0], loc[1]+size//2],         size//2])
                next_waiting.append([[loc[0]+size//2, loc[1]+size//2], size//2])
        
        if len(next_waiting) == 0:
            break
        waiting_list = next_waiting
        
    return answer