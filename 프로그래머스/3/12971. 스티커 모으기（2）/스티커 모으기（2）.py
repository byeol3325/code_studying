def solution(sticker):
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    DP0 = [0]*n
    DP0[0] = sticker[0]
    DP0[1] = sticker[0]
    for i in range(2, n-1):
        DP0[i] = max(DP0[i-2] + sticker[i], DP0[i-1])
    DP0[-1] = DP0[-2]
    
    DP1 = [0]*n
    DP1[0] = 0
    DP1[1] = sticker[1]
    for i in range(2, n):
        DP1[i] = max(DP1[i-2] + sticker[i], DP1[i-1])
    
    return max(DP0[-1], DP1[-1])