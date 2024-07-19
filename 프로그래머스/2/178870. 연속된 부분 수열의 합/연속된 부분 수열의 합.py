def solution(sequence, k):
    n = len(sequence)
    answer = [0, n]
    L, R = 0, 0 # L, R 
    total = sequence[0]
    
    while True:
        if total < k:
            R += 1
            if R == n: # 오른쪽 끝까지 탐색했음
                break
            total += sequence[R] 
        else:
            if total == k:
                if R-L < answer[1] - answer[0]: # 길이가 더 짧음
                    answer = [L, R]
                if R-L == 0: # 가장 짧음
                    break
            total -= sequence[L]
            L += 1
    
    return answer