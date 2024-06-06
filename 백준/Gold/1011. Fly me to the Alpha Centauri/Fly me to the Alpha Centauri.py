import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 0,1 => 0->1 => 1 1
# 0,2 => 0->1->2 => 2 11
# 0,3 => 0->1->2->3 => 3 111
# 1,5 => 1->2->4->5 => 3 121
# 45,50 => 45->46->48->49->50 => 4 1211
# 0,6 => 0->1->3->5->6 => 4 1221    1 = 1
# 0,7 => 0 1 3 5 6 7 12211          11= 2
# 0,8 => 0 1 3 6 7 8 12221          121 = 3
# 0,9 => 0 1 3 6 8 9 12321          1221 = 4
# 0,10 => 0 1 3 6 8 9 10 123211     12321 = 5
# ~~~                    123321     123*2 = 6
#                                   1234 321 = 7
#                                   1234*2 = 8


import math
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    length = y-x
    
    if length == 1:
        print(1)
    elif length == 2:
        print(2)
    else:
        n = int(math.sqrt(length))
        if length <= n**2:
            print(2*n-1)
        elif n**2 < length <= n**2+n:
            print(2*n)
        else:
            print(2*n+1)