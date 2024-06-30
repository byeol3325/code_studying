from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    num_dict = defaultdict(lambda:0)
    for t in tangerine:
        num_dict[t] += 1
        
    num_dict = sorted(num_dict.items(), key = lambda x:(x[1], x[0]), reverse=True)
    
    for i, num in enumerate(num_dict):
        if answer < k:
            answer += num[1]
        else:
            return i
    return len(num_dict)