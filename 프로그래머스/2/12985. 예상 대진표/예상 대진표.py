def solution(n,a,b):
    answer = 0
    # 1 <-> 2, 3 <-> 4, ...
    # 다음 라운드 승자1 <-> 승자2 ...
    all_winers = set() # A와 B는 항상 이김
    all_winers.add(a)
    all_winers.add(b)
    
    # 대진표
    round_info = {} # now_round[번호]: 진짜 번호
    for i in range(1, n+1):
        round_info[i] = i
    
    round_num = 1
    while True:
        next_round_info = {} # [번호]: 진짜 번호
        
        VS = list(round_info.items())
        
        for i in range(len(VS)//2):
            if VS[2*i][1] in all_winers and VS[2*i+1][1] in all_winers:
                return round_num
            
            if VS[2*i+1][1] in all_winers:
                next_round_info[i] = VS[2*i+1][1]
            else:
                next_round_info[i] = VS[2*i][1]
        
        round_info = next_round_info
        round_num += 1
    return answer