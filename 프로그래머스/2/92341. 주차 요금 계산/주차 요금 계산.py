from collections import defaultdict
def read_info(line: str)->list:
    line = line.split()
    time, number, inout = line[0], line[1], line[2]
    
    time = time.split(':')
    minute = int(time[0]) * 60 + int(time[1]) # 계산하기 편하기 위해 분으로 바꾸기
    return [minute, number, inout]

def solution(fees, records):
    answer = []
    
    time_check = defaultdict(lambda:0) # 타임 체크. IN일 때 시간을 저장. OUT일때 비교하기 위해
    total_time = defaultdict(lambda:0)
    
    basic_time, basic_fee = fees[0], fees[1]
    add_time, add_fee = fees[2], fees[3]
    
    for record in records:
        info = read_info(record)
        if info[2] == "IN": # 타임 체크. IN일 때 시간을 저장
            time_check[info[1]] = info[0]
        else:
            total_time[info[1]] += info[0] - time_check[info[1]] # 점유하는 시간 누적시간 체크
            time_check[info[1]] = -1 # 나중에 out 안 되어있는 경우 고려하기 위해
    
    for k, v in time_check.items():
        if v != -1:
            total_time[k] += 23*60 + 59 - v
    
    for k, v in sorted(total_time.items()):
        fee = basic_fee
        if v > basic_time: # 기본 시간을 초과한 만큼 단위 요금 청구 
            fee += (v - basic_time) // add_time * add_fee 
            if (v-basic_time)%add_time != 0: # 나누어 떨어지지 않아서 올림하기 위해
                fee += add_fee
        answer.append(fee)
    return answer