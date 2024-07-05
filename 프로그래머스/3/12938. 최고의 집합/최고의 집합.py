# n 개 중복집합.
# 각 원소 합이 S가 되면서 위 조건을 만족하면서 원소의 곱이 최대가 되는 집합
def solution(n, s):
    if n > s: # 만들숭벗어
        return [-1]
    
    answer = []
    # 2 8 -> 4 4
    # 3 8 -> 2 3 3
    # 4 8 -> 2 2 2 2
    # 5 8 -> 1 1 2 2 2
    # 6 8 -> 1 1 1 1 2 2
    if s%n==0:
        return [s//n]*n
    else:
        answer = [s//n]*n
        res = s - sum(answer)
        for i in range(res):
            answer[-1-i] += 1
    return answer