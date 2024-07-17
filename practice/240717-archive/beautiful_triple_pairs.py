import sys
from collections import defaultdict
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

    c = 0

    d_12 = {}
    d_13 = {}
    d_23 = {}

    for i in range(n-2):
        if (a[i], a[i + 1]) in d_12:
            c += d_12[(a[i], a[i + 1])][1] - d_12[(a[i], a[i + 1])][0][a[i + 2]]
        if (a[i], a[i + 2]) in d_13:
            c += d_13[(a[i], a[i + 2])][1] - d_13[(a[i], a[i + 2])][0][a[i + 1]]
        if (a[i + 1], a[i + 2]) in d_23:
            c += d_23[(a[i + 1], a[i + 2])][1] - d_23[(a[i + 1], a[i + 2])][0][a[i]]
        
        if (a[i], a[i + 1]) not in d_12:
            d_12[(a[i], a[i + 1])] = [defaultdict(lambda: 0), 0]
        if (a[i], a[i + 2]) not in d_13:
            d_13[(a[i], a[i + 2])] = [defaultdict(lambda: 0), 0]
        if (a[i+1], a[i + 2]) not in d_23:
            d_23[(a[i + 1], a[i + 2])] = [defaultdict(lambda: 0), 0]

        d_12[(a[i], a[i + 1])][0][a[i + 2]] += 1
        d_12[(a[i], a[i + 1])][1] += 1
        d_13[(a[i], a[i + 2])][0][a[i + 1]] += 1
        d_13[(a[i], a[i + 2])][1] += 1
        d_23[(a[i + 1], a[i + 2])][0][a[i]] += 1
        d_23[(a[i + 1], a[i + 2])][1] += 1

    
    print(c)