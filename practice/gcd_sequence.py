import sys
from collections import deque, defaultdict
from math import gcd

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

def valid(a):
    prev = gcd(a[0], a[1])
    for i in range(len(a) - 1):
        curr = gcd(a[i], a[i + 1])
        if curr < prev:
            return (False, i)
        
        prev = curr
    return (True, len(a))

for _ in range(inp()):
    n = inp()
    a = inlt()

    is_valid, invalid_idx = valid(a)

    if is_valid:
        print("YES")
        continue
    
    a1 = []
    a2 = []
    a3 = []

    for i in range(n):
        a1.append(a[i])
        a2.append(a[i])
        a3.append(a[i])

        if i == invalid_idx - 1:
            a1.pop()
        
        if i == invalid_idx:
            a2.pop()
        
        if i == invalid_idx + 1:
            a3.pop()
    
    if valid(a1)[0] or valid(a2)[0] or valid(a3)[0]:
        print("YES")
    else:
        print("NO")

