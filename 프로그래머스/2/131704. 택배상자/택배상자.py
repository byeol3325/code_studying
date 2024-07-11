# 택배 상자 크기 같고 1~n까지 번호 증가하는 순서대로 벨트에 일렬로
# 한 방향으로만 진행 가능. 벨트에 놓인 순서대로 상자 내릴 수 있음
# 

from collections import deque

def solution(order):
    answer = 0
    n = len(order)
    belt = deque([i for i in range(1, n+1)])
    order = deque(order)
    
    belt2 = []
    
    while order:
        if belt2 and belt2[-1] == order[0]:
            order.popleft(); belt2.pop()
            answer += 1
        elif belt:
            one = belt.popleft()
            if one == order[0]:
                order.popleft()
                answer += 1
            else:
                belt2.append(one)
        else:
            break
    return answer