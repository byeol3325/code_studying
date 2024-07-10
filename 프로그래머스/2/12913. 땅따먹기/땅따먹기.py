def solution(land):
    answer = 0

    col, row = len(land), len(land[0]) # col = 4로 고정
    DP = [[0]*row for _ in range(col)]
    DP[0] = land[0] # 첫줄 그대로
    
    # DP[i-1][j] + DP[i][j] 는 안됨
    for i in range(1, col):
        for j in range(row):
            DP[i][j] = land[i][j] + max(DP[i-1]) ### j 제외
            if DP[i-1][j] + land[i][j] == DP[i][j]: # j가 포함됨
                DP[i][j] = land[i][j] + max(DP[i-1][:j] + DP[i-1][j+1:])

    return max(DP[-1])