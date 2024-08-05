from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    
    print(q)
    while q:
        # 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
        now_process = q.popleft()
        
        # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        if any(now_process[0] < waiting[0] for waiting in q):
            q.append(now_process)
        else: # 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다
            answer += 1
            if now_process[1] == location:
                return answer
    return answer