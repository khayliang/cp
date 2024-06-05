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
    n = inp()
    a = inlt()
    b = inlt()
    m = inp()
    d = inlt()

    to_change = defaultdict(lambda: 0)
    exists = set()

    for i in range(n):
        exists.add(b[i])
        if a[i] != b[i]:
            to_change[b[i]] += 1

    buffered = False
    
    for i in d:
        if to_change[i] > 0:
            to_change[i] -= 1
            buffered = False
            continue
        if i in exists:
            buffered = False
            continue
        else:
            buffered = True

    if buffered:
        print("NO")
        continue

    failed = False
    
    for i in to_change.values():
        if i != 0:
            failed = True
            break
    
    if failed:
        print("NO")
    else:
        print("YES")


        

