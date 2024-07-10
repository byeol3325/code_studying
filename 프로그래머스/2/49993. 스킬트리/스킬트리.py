def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        idx = 0
        can_skill = 1
        for i in range(len(st)):
            if idx == len(skill): # skill 끝까지 다 배웠음
                break
                
            if st[i] == skill[idx]: # 마침 스킬 찍을 수 있음
                idx += 1
            elif st[i] in skill[idx+1:]: # 뒤에 있어야하는 스킬을 미리 찍음
                can_skill = 0
                break
            else: # 그 외는 패스
                continue
        
        answer += can_skill
    return answer