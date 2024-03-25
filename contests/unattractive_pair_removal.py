import sys
from collections import deque
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

for _ in range(inp()):
    n = inp()
    s = insr()

    if n == 1:
        print(1)

    l = 0
    jumps = deque([])
    r = 1
    removed = 0
    while r < n:
        if s[l] == s[r]:
            if l + 1 == r:
                l += 1
                r += 1
            else:
                jumps.append(l)
                l = r
                r += 1
            continue
        removed += 2
        s[l] = ""
        s[r] = ""
        
        if l == 0:
            r += 2
            l = r - 1
            continue

        r += 1
        if s[l - 1] != "":
            l -= 1
            continue
        
        if len(jumps) == 0:
            r += 1
            l = r - 1
            continue

        l = jumps.pop()        

    print(n - removed)
        
        
