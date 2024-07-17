from math import gcd

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
    mn_a = min(a)
    b = []
    for x in a:
        if x % mn_a != 0:
            b.append(x)
            continue
    
    if (len(b) == 0):
        print("Yes")
        continue

    mn_b = min(b)
    beaut = True
    for x in b:
        if x % mn_b != 0:
            beaut = False
            break
    
    if beaut:
        print("Yes")
    else:
        print("No")
        
        

