from collections import deque

def solution(queue1, queue2):
    answer = -2
    q1, q2 = deque(queue1), deque(queue2)
    # [3,2,7,2], [4,6,5,1] => [2,7,2,4], [6,5,1,3]
    sum_q1, sum_q2 = sum(q1), sum(q2)
    
    cnt = 0
    while cnt <= (len(q1) + len(q2))*2:
        if sum_q1 == sum_q2:
            return cnt
        
        if len(q1) == 0 or len(q2) == 0:
            return -1
        
        if sum_q1 > sum_q2:
            sum_q2 += q1[0]
            sum_q1 -= q1[0]
            q2.append(q1.popleft())
            
        elif sum_q1 < sum_q2:
            sum_q2 -= q2[0]
            sum_q1 += q2[0]
            q1.append(q2.popleft())
        
        cnt+=1

    return -1