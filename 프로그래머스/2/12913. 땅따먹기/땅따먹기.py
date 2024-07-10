def solution(land):
    answer = 0

    col, row = len(land), len(land[0]) # col = 4로 고정
    DP = [[0]*row for _ in range(col)]
    DP[0] = land[0] # 첫줄 그대로
    
    
    # DP[i-1][j] + DP[i][j] 는 안됨
    for i in range(1, col):
        for j in range(row):
            pri_DP = DP[i-1].copy()
            pri_DP[j] = 0 # j 제외
            DP[i][j] = land[i][j] + max(pri_DP)

    
    return max(DP[-1])