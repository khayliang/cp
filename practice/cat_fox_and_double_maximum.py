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
    p = inlt()
    a = [0] * n

    n_idx = 0
    for i in range(n):
        if p[i] == n:
            n_idx = i
            break

    peaks = []
    non_peaks = []
    
    for i in range(n):
        if n_idx % 2 != 0 and i % 2 != 0:
            peaks.append((p[i], i))
        elif n_idx % 2 == 0 and i % 2 == 0:
            peaks.append((p[i], i))
        else:
            non_peaks.append((p[i], i))
    
    peaks.sort(key=lambda x: x[0])
    non_peaks.sort(key=lambda x: x[0])

    k = n
    for _, i in peaks:
        a[i] = k
        k -= 1
    
    for _, i in non_peaks:
        a[i] = k
        k -= 1
    
    print(*a)