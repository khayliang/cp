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
    n, m, k = inlt()
    c_max = defaultdict(lambda: (-1, -1))
    a = [0] * k
    for i in range(k):
        r, c = inlt()
        if c_max[c - 1][0] < r - 1:
            c_max[c - 1] = (r - 1, i)

    mn_c = min(c_max.keys())

    r = -1
    c = 0

    area = 0

    if mn_c == 0:
        mn_r = c_max[0][0]
        a[c_max[0][1]] = 1
        r = mn_r
        c = mn_c

    
    for f_c in sorted(c_max.keys()):
        if f_c == 0:
            continue

        f_r = c_max[f_c][0]

        if f_r <= r:
            continue
        
        a[c_max[f_c][1]] = 1
        area += (f_c) * (f_r - r)
        r = f_r
        c = f_c
    
    area += m * (n - 1 - r)
    print(area)
    print(*a)

    
