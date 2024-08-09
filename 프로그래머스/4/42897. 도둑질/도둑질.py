def solution(money):
    answer = 0
    n = len(money)
    
    if n == 1:
        return money[0]
    
    # 첫 집 털기 => 마지막 집은 털지 않기
    DP = [[0, 0] for _ in range(n-1)]
    DP[0][1] = money[0]
    for i in range(1, n-1):
        DP[i][0] = max(DP[i-1])
        DP[i][1] = DP[i-1][0] + money[i]
    
    # 첫 집 안 털었음 => 마지막 집은 털지 않기
    DP_0 = [[0, 0] for _ in range(n)]
    for i in range(1, n):
        DP_0[i][0] = max(DP_0[i-1])
        DP_0[i][1] = DP_0[i-1][0] + money[i]
    
    return max(max(DP[-1]), max(DP_0[-1]))