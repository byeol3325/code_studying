# x -> y 변환
# x + n / x*2 / x*3
# 최소 연산 횟수 return
from collections import deque

def solution(x, y, n):
    """
    x -> y로 변환
    x + n / x*2 / x*3. 최소 연산 횟수 return. 만들 수 없으면 return
    y -> x로 가자
    """    
    q = deque()
    q.append((y, 0)) # 수, cnt
    
    while q:
        num, cnt = q.popleft()
        
        if num < x:
            continue
        
        if num == x:
            return cnt
        
        if (num / 3 == x) or (num / 2 == x) or num - n == x:
            return cnt + 1
        
        if num%3 == 0:
            q.append((num//3, cnt+1))
        if num%2 == 0:
            q.append((num//2, cnt+1))
        q.append((num-n, cnt+1))
    return -1