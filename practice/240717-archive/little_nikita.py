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
    n, m = inlt()
    if m > n:
        print("No")
        continue
    
    if m == n:
        print("Yes")
        continue
    
    if n % 2 == m % 2:
        print("Yes")
    else:
        print("No")