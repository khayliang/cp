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

def sol(k, s):
    curr_b = 0
    for c in s:
        if c == 'B':
            curr_b += 1
    if curr_b == k:
        return (-1, 'A')
    if curr_b > k:
        diff = curr_b - k
        for i, c in enumerate(s):
            if diff == 0:
                return (i, 'A')
            if c == 'B':
                diff -= 1
    if curr_b < k:
        diff = k - curr_b
        for i, c in enumerate(s):
            if diff == 0:
                return (i, 'B')
            if c == 'A':
                diff -= 1
    
    

cases = inp()
for i in range(cases):
    n, k = inlt()
    s = input()
    x, ch = sol(k, s)
    if (x == -1):
        print(0)
    else:
        print(1)
        print(str(x) + " " + ch)