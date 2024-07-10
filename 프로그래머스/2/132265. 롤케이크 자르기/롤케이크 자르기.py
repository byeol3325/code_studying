from collections import Counter

def solution(topping):
    answer = 0
    
    count_dict = Counter(topping)
    brother_set = set()
    
    for t in topping:
        count_dict[t] -= 1
        if count_dict[t] == 0:
            del count_dict[t]
        brother_set.add(t)
        
        if len(count_dict) == len(brother_set):
            answer += 1
    """
    시간 초과
    answer = 0
    for i in range(1, len(topping)):
        set1, set2 = set(topping[:i]), set(topping[i:])
        if len(set1) == len(set2):
            answer += 1
    """
    return answer