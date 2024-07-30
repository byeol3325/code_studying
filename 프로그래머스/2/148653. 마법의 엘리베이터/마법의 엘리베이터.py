def solution(storey):
    answer = 0
    
    # 합이 음수면 움직이지 않음
    # 규칙이 존재함.
    cnt = 0
    while storey != 0:
        if storey%10 < 5:
            cnt += storey%10
            storey = storey//10
        elif storey%10 > 5:
            cnt += (10 - storey%10)
            storey = storey//10 + 1
        else: # storey%10 == 5:
            if (storey//10)%10 >= 5:
                cnt += (10 - storey%10)
                storey = storey//10 + 1
            else:
                cnt += storey%10
                storey = storey//10
    return cnt