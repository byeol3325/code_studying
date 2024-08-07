DP = [0] * 60001
DP[1] = 1
DP[2] = 2
def solution(n):
    if DP[n] != 0:
        return DP[n]
    
    for i in range(3, n+1):
        DP[i] = (DP[i-1] + DP[i-2])%(10**9+7)

    return DP[n]