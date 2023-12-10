import sys
from collections import deque
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

cases = inp()
for _ in range(cases):
    s = insr()
    upper = deque([])
    lower = deque([])
    new_s = ['' for _ in s]
    for i, c in enumerate(s):
        if c == 'B':
            if len(upper) != 0:
                i = upper.pop()
                new_s[i] = ''
            continue
        if c == 'b':
            if len(lower) != 0:
                i = lower.pop()
                new_s[i] = ''
            continue
        new_s[i] = c
        if c.isupper():
            upper.append(i)
        if c.islower():
            lower.append(i)
    print(''.join(new_s))
            
