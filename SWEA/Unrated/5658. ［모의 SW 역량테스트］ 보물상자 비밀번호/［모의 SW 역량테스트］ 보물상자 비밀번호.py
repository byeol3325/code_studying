T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def sol(N, K, Nums):
    l = N//4
    all_ = set()
    
    for i in range(l):
        nNums = Nums[i:] + Nums[:i+1]
        for j in range(4):
            all_.add(int(nNums[j*l:(j+1)*l],16))

    all_ = sorted(all_, reverse=True)
    return all_[K-1]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    Nums = input()
    print("#%d %d" %(test_case, sol(N, K, Nums)))
