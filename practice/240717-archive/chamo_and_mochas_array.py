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


for _ in range(inp()):
    n = inp()
    a = inlt()
    mx = 0
    if n == 2:
        print(min(a))
        continue
        
    for i in range(n - 2):
        s = list(a[i:i + 3])
        s.sort()
        mx = max(mx, s[1])

    print(mx) 