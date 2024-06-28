# 멘토 n명. 1~k번 상담 유형. 각 멘토는 k개 상담 유형 중 하나만 담당
# 멘토는 자신이 담당하는 유형의 상담만 가능. 다른 유형의 상담은 불가능
# 멘토는 참가자 한명과 상담 가능. 상담 시간은 참가자가 요청한 시간만큼

# 참가자가 상담 요청하면
# 1. 상담을 원하는 참가자가 상담 요청했을 때, 참가자의 상담 유형을 담당하는 멘토 중
#    상담 중이 아닌 멘토와 상담 시작.
# 2. 모든 멘토가 상담 중이라면, 자신의 차례가 올 때까지 기다리기. 참가자가 기다린 시간은
#    상담 요청했을 때부터 멘토와 상담을 시작할 때까지의 시간.
# 3. 모든 멘토는 상담이 끝났을 때 자신의 상담 유형의 상담을 받기 위해 기다리고 있는
#    참가자가 있으면 즉시 상담을 시작. 이때, 먼저 상담 요청한 참가자가 우선.

# 참가자의 상담 요청 정보가 주어질 때, 참가자가 상담을 요청했을 때부터 상담을 시작하기까지
# '기다린 시간의 합의 최소'가 되도록 각 상담 유형별로 멘토 인원을 정하려 합니다.
# 각 유형별로 멘토 인원 적어도 한명 이상이어야함.
import heapq as hq

def solve(n: int, waiting: list) -> int:
    """
    waiting 을 n명의 상담원으로 최소 대기시간
    """
    answer = 0
    if n >= len(waiting): # 상담원 수 >= 기다리는 사람 수
        return answer
    
    mento = [0]*n
    for one in waiting:
        mento_endtime = hq.heappop(mento)
        
        if mento_endtime > one[0]: # 기다렸다면 기다린 시간 추가
            answer += (mento_endtime - one[0])
            hq.heappush(mento, mento_endtime + one[1]) # 끝난 시간은 heap에 넣어주기
        else:
            hq.heappush(mento, one[0] + one[1]) # 끝난 시간은 heap에 넣어주기
    return answer

def backtracking_permutations(k: int, mento_list: list):
    result = []
    n = len(mento_list)
    distribution = mento_list.copy()
    indices = [i for i in range(n) if mento_list[i] != 0] # 상담 유형 있는 곳만 채우기
    
    def backtrack(idx: int, remaining_mentos: int):
        if idx == len(indices) - 1:
            distribution[indices[idx]] += remaining_mentos
            result.append(distribution.copy())
            distribution[indices[idx]] -= remaining_mentos
            return
        
        for i in range(remaining_mentos + 1):
            distribution[indices[idx]] += i
            backtrack(idx + 1, remaining_mentos - i)
            distribution[indices[idx]] -= i
    
    backtrack(0, k)
    
    return result
    
min_time = float("inf")
def solution(k: int, n: int, reqs: list) -> int:
    global min_time
    
    answer = 0
    
    waiting_queue = [[] for _ in range(k+1)] # k번째 waiting
    for req in reqs:
        waiting_queue[req[2]].append(req[:2])
    
    # backtracking을 위한 초기값 설정
    remaining_mentos = n - k
    mento_list = [1] * (k+1) # 각 유형별로 멘토 인원이 적어도 한명 이상이어야함
    mento_list[0] = 0
    
    mento_lists = backtracking_permutations(remaining_mentos, mento_list) # 모든 가능한 경우의 수
    print(mento_lists)
    
    for ml in mento_lists: # [0, 1, 3, 2] ...
        waiting_time = 0
        for i, m in enumerate(ml): # 1, 3, ...
            if m == 0:
                continue
            waiting_time += solve(m, waiting_queue[i])
            
            if waiting_time > min_time: # 이미 시간이 길면 다음 mento_list 확인
                break
        min_time = min(min_time, waiting_time)
    
    
    return min_time