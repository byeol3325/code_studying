def solution(n,a,b):
    answer = 1
    
    while True:
        next_a, next_b = (a+1)//2, (b+1)//2
        if next_a == next_b:
            return answer
        else:
            a, b = next_a, next_b
            answer += 1
    return answer