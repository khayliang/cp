import sys
from collections import deque, defaultdict
import math

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

# amt to remove from smaller number
def amt_to_remove(s, l):
    s_len = int(math.log2(s)) + 1
    l_len = int(math.log2(l)) + 1

    x = l >> (l_len - s_len)
    y = x ^ s

    if y == 0:
        return 0
    
    return int(math.log2(y)) + 1

# amt to add to smaller number supposing the smaller's been removed
def amt_to_add(s, l):
    s_len = int(math.log2(s)) + 1
    l_len = int(math.log2(l)) + 1

    return l_len - s_len

def get_next_no(a, n, start):
    for i in range(start, n):
        if a[i] != -1:
            return i
    return n

def tf(s, l):
    b = []

    x = amt_to_remove(s, l)

    for i in range(x):
        s = s >> 1
        b.append(s)

    x = amt_to_add(s, l)
    
    for i in range(x - 1, -1, -1):
        b.append(l >> i)
    return b

def solve(n, a_p):
    # settle first no
    first_no_idx = get_next_no(a_p, n, 0)

    if first_no_idx == n:
        return [1 if i % 2 == 0 else 2 for i in range(n)]
    

    first_no = a_p[first_no_idx]
    toggle = True
    for i in range(first_no_idx - 1, -1, -1):
        if toggle:
            a_p[i] = first_no * 2
        else:
            a_p[i] = first_no
        toggle = not toggle
    
    curr_no_idx = first_no_idx
    next_no_idx = get_next_no(a_p, n, curr_no_idx + 1)
    while next_no_idx < n:
        curr_no = a_p[curr_no_idx]
        next_no = a_p[next_no_idx]
        if curr_no_idx + 1 == next_no_idx:
            if curr_no * 2 + 1 == next_no or\
            curr_no * 2 == next_no or\
            curr_no // 2 == next_no:
                curr_no_idx += 1
                next_no_idx = get_next_no(a_p, n, curr_no_idx + 1)
                continue
        
        s = min(a_p[curr_no_idx], a_p[next_no_idx])
        l = max(a_p[curr_no_idx], a_p[next_no_idx])

        if s == l:
            toggle = True
            for i in range(curr_no_idx + 1, next_no_idx):
                if toggle:
                    a_p[i] = s * 2
                else:
                    a_p[i] = s
                toggle = not toggle

            if a_p[next_no_idx] == a_p[next_no_idx - 1]:
                return -1
            
            curr_no_idx = next_no_idx
        else:
            b = tf(s, l)
                
            if len(b) > next_no_idx - curr_no_idx:
                return -1
            
            if a_p[curr_no_idx] < a_p[next_no_idx]:
                for i in range(len(b)):
                    a_p[curr_no_idx + 1 + i] = b[i]
                curr_no_idx = curr_no_idx + len(b)

            else:
                for i in range(len(b)):
                    a_p[next_no_idx - 1 -i] = b[i]

        next_no_idx = get_next_no(a_p, n, curr_no_idx + 1)
    
    if curr_no_idx < n - 1:
        curr_no = a_p[curr_no_idx]
        toggle = True

        for i in range(curr_no_idx + 1, n):
            if toggle:
                a_p[i] = curr_no * 2
            else:
                a_p[i] = curr_no
            toggle = not toggle

    return a_p
    

for _ in range(inp()):
    n = inp()
    a_p = inlt()

    res = solve(n, a_p)
    if res == -1:
        print(res)
    else:
        print(*res)

