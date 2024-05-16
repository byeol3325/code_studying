n, k = map(int, input().split())
Values = [int(input()) for _ in range(n)]
# N가지 종류 동전. 각각 동전의 가치는 다름. 동전 적당히 사용해서 그 가치의 합이 k원이 되도록 하고 싶음.
# 경우의 수를 구하시오. 각각의 동전은 몇개라도 사용 가능
# 사용한 동전의 구성이 같은데 다른 것은 같은 경우

Values.sort()

# DP 배열 초기화
DP = [0]*(k+1)
DP = [0] * (k + 1)
DP[0] = 1  # 0원을 만드는 경우의 수는 항상 1

for v in Values:
    for j in range(v, k + 1):
        DP[j] += DP[j - v]

print(DP[k])