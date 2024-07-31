from collections import deque
from copy import deepcopy

def get_info(line):
    """
    string을 잘라서 [숫자, 연산자, 숫자 ...] 로 자르기
    연산자 종류에 operator 넣기
    """
    array = deque()
    num_start = ""
    operator = set()
    for e in line:
        if e == "+" or e == "-" or e == "*":
            array.append(int(num_start))
            array.append(e)
            operator.add(e)
            num_start = ""
        else:
            num_start += e
    array.append(int(num_start))
    return array, operator

def do_compute(array, operator):
    operator = list(operator)
    answer = -float("inf")
    if len(operator) == 0:
        return array[0]
    else:
        cases = permutation(operator)
        for case in cases:
            case = deque(case) # 우선순위
            
            result = None
            now_array = deepcopy(array)
            while case:
                one_oper = case.popleft()
                now_array = do_compute_oper(now_array, one_oper)
            result = now_array[0]
            answer = max(answer, abs(result))
    return answer

def do_compute_oper(array: list, oper: str):
    next_deque = deque()
    while array:
        one = array.popleft()
        if len(next_deque) == 0:
            next_deque.append(one)
        elif one == oper:
            if one == "-":
                next_deque[-1] -= array.popleft()
            elif one == "+":
                next_deque[-1]  += array.popleft()
            else: # one == "*":
                next_deque[-1]  *= array.popleft()
        else: # one != oper
            next_deque.append(one)
    return next_deque
            

def permutation(operator):
    n = len(operator)
    visited = [0]*n
    results = []
    def make(one):
        nonlocal visited, n, operator, results
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                one.append(operator[i])
                if len(one) == n:
                    results.append(deepcopy(one))
                else:
                    make(one)
                visited[i] = 0
                one.pop()
        return None
    make([])
    return results    

def solution(expression):
    array, operator = get_info(expression)    
    answer = do_compute(array, operator)
    return answer