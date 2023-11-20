import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

def sol(l):
    prev = 0
    for i in l:
        if prev == 0:
            if i != 1:
                prev = 1
                continue
            prev = 2
            continue
        if i == prev + 1:
            prev = prev + 2
            continue
        prev = prev + 1
    return prev
        
cases = inp()

for i in range(cases):
    n = inp()
    print(sol(inlt()))
