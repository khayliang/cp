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

    best_y = 0
    mx = 0
    for i in range(1,n + 1):
        if (n % i == 0):
            y = ((n // i) - 1) * i
            if (i + y > mx):
                best_y = y
                mx = i + y
    print(best_y)