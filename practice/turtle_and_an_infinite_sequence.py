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

    if m == 0:
        print(n)
        continue

    l = n - m
    r = n + m
    if len(bin(l)) != len(bin(r)):
        print(pow(2, len(bin(r)) - 2) - 1)
        continue
        

    stopped_i = -1
    bin_l = bin(l)
    bin_r = bin(r)
    for i in range(2, len(bin_l)):
        if bin_l[i] != bin_r[i]:
            stopped_i = i
            break
    
    res = []
    changed = False
    for i in range(2, len(bin_r)):
        if changed:
            res.append("1")
            continue
        if bin_l[i] == bin_r[i]:
            res.append(bin_l[i])
        else:
            changed = True
            res.append("1")
    print(int(''.join(res), 2))
        
