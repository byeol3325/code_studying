def solution(msg):
    answer = []
    DICTIONARY = {}
    
    for i in range(65, 91): # DICTIONARY['A'] = 1 ~ DICTIONARY['Z'] = 26 초기화
        DICTIONARY[chr(i)] = i-64
    
    word_idx = 27
    start = 0
    l = 1
    cnt = 0
    while True:
        if start == len(msg)-1:
            answer.append(DICTIONARY[msg[-1]])
            break
        
        if start + l >= len(msg):
            answer.append(DICTIONARY[msg[start:]])
            break
        
        if msg[start:start+l+1] not in DICTIONARY:
            answer.append(DICTIONARY[msg[start:start+l]])
            DICTIONARY[msg[start:start+l+1]] = word_idx
            word_idx += 1
            start += l # 다음 start 지목
            l = 1 # 초기화
        else:
            l += 1
        
    return answer