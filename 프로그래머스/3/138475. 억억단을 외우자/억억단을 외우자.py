# e이하 임의의 수 s. s에 대해 s보다 크고 e보다 작은 수 중에서 억억단에서 가장 많이 등장한 수
# 가장 많이 등장한 수가 여러 개라면 그 중 가장 작은 수
def get_divisor_list(starts: list, end: int) -> list:
    divisor_list = [0]*(end+1)
    for i in range(1, int(end**0.5)+1):
        divisor_list[i*i] += 1
        for j in range(i*(i+1), end+1, i):
            divisor_list[j] += 2
    return divisor_list

def solution(end: int , starts: list) -> int:
    """
    start 수보다 뒤에 있는 수 들 중에 가장 약수 갯수가 많은 수. 약수 갯수가 같다면 가장 작은 수
    """
    divisor_list = get_divisor_list(starts, end)
                
    min_start = min(starts) # starts : list 에서 가장 작은 수
    result_info = [0]*(end+1) # result_info[start] = result
    
    max_div_list = [0]*(end+1)
    max_div_list[-1] = end
    for i in range(end-1, 0, -1) :
        if divisor_list[max_div_list[i+1]] <= divisor_list[i] :
            max_div_list[i] = i
        else :
            max_div_list[i] = max_div_list[i+1]
    
    return [ max_div_list[s] for s in starts ]