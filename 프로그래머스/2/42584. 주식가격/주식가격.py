from collections import deque

def solution(prices):
    """
    초 단위로 기록된 주식이 담긴 배열 prices 가격이 떨어지지 않은 기간이 몇 초인지 return
    """
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        time = 0
        for j in range(i+1, n, 1):
            if prices[i] <= prices[j]:
                time += 1
            else:
                answer[i] = time + 1
                break
            
            if j == n-1:
                answer[i] = time
    return answer