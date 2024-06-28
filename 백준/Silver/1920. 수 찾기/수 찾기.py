N = int(input())
Ns = set(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

for m in Ms:
    if m in Ns:
        print(1)
    else:
        print(0)