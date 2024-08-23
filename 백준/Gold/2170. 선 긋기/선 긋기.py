import sys
input = sys.stdin.readline

n = int(input())
lines = []
ans = 0

for _ in range (n) :
    lines.append(tuple(map(int, input().split())))


# 정렬을 해주면 start는 비교할 필요가 없음
lines.sort()

# start가 가장 작은 점을 기준으로
start,end = lines[0]


for i in range(1,n) :
    x,y=lines[i]

    # 겹치는 경우
    if x <= end :
        end = max(y, end)
    # 아예 겹치지 않는 경우
    else :
        ans += (end - start) # 기존의 차이를 더해주고
        start, end = x, y # 시작,끝점 새롭게 업데이트
    
ans += (end - start)
print(ans)