from collections import defaultdict
from itertools import combinations

def solution(orders: list, course: list):
    answer = []
    
    comb = combinations(orders[0], 2)
    for c in course:
        NUM_DICT = defaultdict(lambda:0)
        for order in orders:
            comb = combinations(order, c)
            for com in comb:
                NUM_DICT[''.join(sorted(com))] += 1
        NUM_DICT = sorted(NUM_DICT.items(), key=lambda x:(x[1], x[0]), reverse=True)
        
        answer += [menu for menu, cnt in NUM_DICT if cnt > 1 and NUM_DICT[0][1] == cnt]
    return sorted(answer)