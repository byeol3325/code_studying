import sys
input = sys.stdin.readline

N = int(input())
Ns = list(map(int, input().split())); Ns.sort()
M = int(input())
Ms = list(map(int, input().split()))

def binarySearch(t):
    global N, Ns, M, Ms
    
    start = 0; end = N-1;
    while start <= end:
        mid = (start+end)//2
        if Ns[mid] == t:
            return True
        elif Ns[mid] > t:
            end = mid-1
        else:
            start = mid+1
    return 

def Search(): # Ms, Ns
    global N, Ns, M, Ms
    
    for m in Ms:
        if binarySearch(m): 
            print(1)
        else: 
            print(0)

Search()