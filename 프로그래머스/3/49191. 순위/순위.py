# 권투선수 1~n
# 1:1, A > B 실력. A 항상 이김
# 결과로 순위 메기기.
# 몇몇 경기 결과 분실.
# 순위 메길 수 있는 선수 return

# 선수 수. 1 <= n <= 100
# 경기 결과. 1 <= len(results) <= 4500
# [A,B] => A가 B 이김

from collections import deque

def solution(n, results):
    answer = 0
    ranks = [0]*(n+1)
    
    wins = {i: set() for i in range(1, n+1)}
    losers = {i: set() for i in range(1, n+1)}
    
    for w, l in results:
        wins[w].add(l); losers[l].add(w)
    
    for i in range(1, n+1):
        for l in wins[i]:
            losers[l] |= losers[i]
        for w in losers[i]:
            wins[w] |= wins[i]
    
    for i in range(1, n+1):
        if len(wins[i]) + len(losers[i]) == n-1:
            answer += 1
    
    return answer