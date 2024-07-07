def N_number(n, num):
    """
    num 을 n 진수로 변환
    """
    if num == 0:
        return "0"
    
    num_string = "0123456789ABCDEF"
    n_number = ""
    next_n = n
    while True:
        if num == 0:
            break
        now_digit = num%n
        num = num // n
        next_n = next_n * n
        n_number = num_string[now_digit] + n_number
    
    return n_number


def solution(n, t, m, p):
    answer = ''
    
    idx = p-1
    total = ""
    number = 0
    while True:
        n_number = N_number(n, number)
        total += n_number
        number += 1
        
        if len(total) >= m*t + p:
            break

    for i in range(t):
        answer += total[i*m + (p-1)]
        
    return answer