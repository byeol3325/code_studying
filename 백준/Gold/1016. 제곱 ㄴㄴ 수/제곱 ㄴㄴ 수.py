x, y = map(int, input().split())

nono = [1]*(y-x+1)

idx = 2
while idx <= int(y**0.5):
    p = idx**2
    tmp = (x//p)*p
    while tmp <= y:
        if x <= tmp:
            nono[tmp-x] = 0
        tmp += p
    idx += 1

print(sum(nono))