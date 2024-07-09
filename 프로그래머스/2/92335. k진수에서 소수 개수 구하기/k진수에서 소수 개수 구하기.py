def N_number(num, n):
    """
    num을 n진법 수로 바꾸기
    """
    num_str = "0123456789"
    n_num = ""
    
    next_n = n
    while True:
        if num == 0 or next_n == 81:
            break

        n_num = num_str[num % n] + n_num
        num = num // n
        
    return n_num

def is_prime(num):
    """
    소수인지 아닌지 
    """
    if num == '' or num == '1':
        return False
    
    num = int(num)
    mid = int(num**0.5) + 1
    
    for i in range(2, mid):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    n_number = N_number(n, k)
    n_number_split0 = n_number.split('0') # 0 제외
    
    for s in n_number_split0:
        if is_prime(s):
            answer += 1
    
    return answer