def solution(cap, n, deliveries, pickups):
    answer = 0
    
    del_idx, pick_idx = -1,-1 # 어디서부터 시작할지 idx 찾기
    for i in range(n-1, -1, -1):
        if deliveries[i] != 0 and del_idx == -1:
            del_idx = i
        if pickups[i] != 0 and pick_idx == -1:
            pick_idx = i
        
        if del_idx != -1 and pick_idx != -1:
            break
    #print(del_idx, pick_idx)
    def next_idx(lists_: list, idx: int):
        total_ = 0
        max_length = 0
        if idx == -1:
            return lists_, idx, 0

        while total_ < cap:
            if lists_[idx] == 0:
                idx -= 1
                if idx == -1:
                    break
                continue
            
            if total_ + lists_[idx] > cap:
                if max_length == 0:
                    max_length = idx
                lists_[idx] -= (cap - total_)
                total_ = cap
                break
            else:
                if max_length == 0:
                    max_length = idx
                total_ += lists_[idx]
                lists_[idx] = 0
                idx -= 1
            
            if idx == -1:
                break

        if total_ == 0:
            max_length = -1

        return lists_, idx, max_length+1
    
    cnt = 0
    while True:
        cnt+=1
        if del_idx == -1 and pick_idx == -1: # 끝까지 다 확인함
            break
        
        deliveries, del_idx, del_move = next_idx(deliveries, del_idx)
        pickups, pick_idx, pick_move = next_idx(pickups, pick_idx)
        
        answer += max(del_move, pick_move)*2
        #print("======================= HERE =======================")
        #print(deliveries, del_idx, del_move)
        #print(pickups, pick_idx, pick_move)
    return answer