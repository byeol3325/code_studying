def solution(N, number):
    # 최대 사용 횟수
    MAX_COUNT = 8
    
    # DP를 위한 set 초기화
    dp = [set() for _ in range(MAX_COUNT + 1)]
    
    # 각 숫자마다의 set 초기화
    for i in range(1, MAX_COUNT + 1):
        dp[i].add(int(str(N) * i))
    
    # 주어진 수에 도달할 때까지 반복
    for i in range(1, MAX_COUNT + 1):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        print(dp)
        # 주어진 수를 만들 수 있는지 확인
        if number in dp[i]:
            return i
    
    # 만들 수 없는 경우 -1 반환
    return -1