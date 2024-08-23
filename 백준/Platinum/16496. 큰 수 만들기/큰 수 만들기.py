import sys
input = sys.stdin.readline

n = int(input())

lst = input().split()
q = max(map(lambda x : len(x),lst))
lst.sort(key= lambda x : int(x.ljust(q,'0')) ,reverse=True    )
ans = ""
for x in lst:
    ans = max(x+ans,ans+x)
if int(ans) == 0:
    print(0)
else:
    print(ans)  