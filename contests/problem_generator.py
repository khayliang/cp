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
    a = insr()
    d = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0
    }

    for i in a:
        d[i] += 1

    amt = 0
    for i in range(m):
        if d['A'] == 0:
            amt += 1
        else:
            d['A'] -= 1
        if d['B'] == 0:
            amt += 1
        else:
            d['B'] -= 1
        if d['C'] == 0:
            amt += 1
        else:
            d['C'] -= 1
        if d['D'] == 0:
            amt += 1
        else:
            d['D'] -= 1
        if d['E'] == 0:
            amt += 1
        else:
            d['E'] -= 1
        if d['F'] == 0:
            amt += 1
        else:
            d['F'] -= 1
        if d['G'] == 0:
            amt += 1
        else:
            d['G'] -= 1 

    print(amt)