# ATM 앞에 N명
# 사람들은 1~N번까지 번호
# i번째 사람이 돈인출하는데 걸리는 시간은 P_i
# P = [3,1,4,3,2]이고 12345순으로 서면 1번사람은 3분만에 돈을 뽑고
# 2번사람은 3+1분
# 돈을 인출하는데 총 걸리는시간은 3+4+8+11+13 = 39
# 모든 사람이 인출하는데 최솟값을 구하도록 가즈아앙

N = int(input())
times = list(map(int, input().split()))
times.sort()

totalTime = 0
for i in range(N):
    totalTime += (N-i)*times[i]

print(totalTime)