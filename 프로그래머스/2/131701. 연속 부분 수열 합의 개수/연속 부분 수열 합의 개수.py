def solution(elements):
    answer = 0
    cycle_elements = elements + elements
    
    n = len(elements)
    total = set()
    for i in range(n):
        one = elements[i]
        total.add(one)
        for j in range(i+1, i+n):
            one += cycle_elements[j]
            total.add(one)
    
    return len(total)