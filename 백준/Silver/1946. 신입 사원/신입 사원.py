# 1차 서류
# 2차 면접
# 다른 지원자와 비교했을 때 서류심자 / 면접 시험 중 하나가 다른 지원자보다 떨어지지 않는 자만 선발
# A 지원자 성적이 다른 B 성적에 비해 모두 떨어지면 선발 X
import sys
input = sys.stdin.readline
T = int(input())

def solution(N: int, scores: list)->int:
    scores.sort()
    answer = 1 # 맨 위 1등은 합격
    top = 0
    for i in range(1, N):
        # i가 자신보다 scores[][0]이 높은 사람들에서 가장 [1]이 낮은 사람보다 점수 높은지 확인
        if scores[i][1] < scores[top][1]: 
            top = i
            answer += 1            
    return answer

for test_case in range(1, T+1):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, scores))