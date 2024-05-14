# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
 
# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''
 
# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''
 
 
 
 
'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
def change(numList, cnt):
    idx = 0
    n = len(numList)
    start = 0 # max_가 여러개면 고려해야함 ㅠ
    res = [] # max_가 여러개면 고려해야함 ㅠ
    while cnt != 0: # cnt가 0이 되거나 idx 가 n-1이상이 되면 while 나와야함
        max_ = max(numList[idx+1:])
        if numList[idx] < max_: # 크면 바꿔줘야함. cnt -=1 해줘야함
            max_idxs = [i for i in range(idx+1, n) if numList[i] == max_] # 같은 max 중에 뒤에꺼로 바꿔줘야함
            if len(max_idxs) != 1: # max_가 여러개면 조금 고려해야함
                numList[max_idxs[-1]] = numList[idx]
                numList[idx] = max_ # 값 바꾸기
                res.append(max_idxs[-1])
                cnt -= 1
            else:
                numList[max_idxs[-1]] = numList[idx]
                numList[idx] = max_ # 값 바꾸기
                cnt -= 1 # 바꾸기 1회 차감
        else:
            pass
        idx += 1 # 다음꺼 가야지. 반드시 가야지
         
        if idx == n-1: # 끝까지했는데도 없으면 일단 나와야함
            break
    if res != []: # 겹치는애들 순서 바꿔줘야함
        res_value = [numList[i] for i in res]
        res.sort()
        res_value.sort(reverse=True)
        for i in range(len(res)):
            numList[res[i]] = res_value[i]
     
    if cnt != 0: # 더 바꿔줘야함 끝에꺼만 ㄱㄱ
        max_ = max(numList)
        max_idxs = [i for i in range(n) if numList[i] == max_]
        if len(max_idxs) > 1:
            return numList
        while cnt != 0:
            a = numList[n-2]
            numList[n-2] = numList[n-1]; numList[n-1] = a
            cnt -= 1        
    return numList
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    line = input().split()
    numList = list(line[0]);  cnt = int(line[1])
    numList = change(numList, cnt)
    result = "#" + str(test_case) + " " + ''.join(numList)
    print(result)
    '''
 
        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
 
    '''
    # ///////////////////////////////////////////////////////////////////////////////////