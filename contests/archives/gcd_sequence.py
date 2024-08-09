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

for _ in range(inp()):
    n = inp()
    a = inlt()
    
    prev = 0
    prev_prev = 0
    failed = False
    actually_failed = False
    for i in range(n - 1):
        curr = gcd(a[i], a[i + 1])

        if curr >= prev:
            prev_prev = prev
            prev = curr
            continue
        
        
        if failed:
            actually_failed = True
            break
        
        failed = True

        best_curr = float('inf')

        
        new_prev = gcd(a[i - 2], a[i])
        # check prev prev
        if i - 3 >= 0 \
        and gcd(a[i - 3], a[i - 2]) <= new_prev \
        and curr >= new_prev:
            best_curr = curr
        elif i - 3 < 0 and i - 2 >= 0 \
        and curr > new_prev:
            best_curr = curr
        elif i - 1 == 0:
            best_curr = curr


        # try i
        curr = gcd(a[i - 1], a[i + 1])
        if curr >= prev_prev:
            best_curr = min(curr, best_curr)

        # try i + 1
        if i + 2 == n:
            break
        
        if i + 2 < n:
            curr = gcd(a[i], a[i + 2])
            if curr >= prev and curr < best_curr:
                best_curr = curr
                a[i + 1] = a[i]

        if best_curr != float('inf'):
            prev_prev = prev
            prev = best_curr
            continue

        actually_failed = True
        break

    if actually_failed:
        print("NO")
    else:
        print("YES")
    

