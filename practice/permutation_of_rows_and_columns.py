import sys
from collections import deque, defaultdict

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
    a = [inlt() for _ in range(n)]
    b = [inlt() for _ in range(n)]

    failed = False

    a_idx = [0] * (n * m + 1)

    for i in range(n):
        for j in range(m):
            a_idx[a[i][j]] = (i, j)
    
    failed = False
    # check row
    for i in range(n):
        r = a_idx[b[i][0]][0]
        for j in range(m):
            if a_idx[b[i][j]][0] != r:
                failed = True
                break
        if failed:
            break
    
    if failed:
        print("NO")
        continue
    
    # check col
    for j in range(m):
        c = a_idx[b[0][j]][1]
        for i in range(n):
            if a_idx[b[i][j]][1] != c:
                failed = True
                break
        if failed:
            break

    if failed:
        print("NO")
    else:
        print("YES")