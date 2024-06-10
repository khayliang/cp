import sys
from collections import deque, defaultdict
from math import lcm, sqrt

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

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    set_a = set(a)

    mx = max(a)

    if lcm(*a) > mx:
        yield n
        return

    mx_len = 0
    for i in range(1, int(sqrt(mx)) + 2):
        if mx % i == 0:
            if i not in set_a:
                LCM = 0
                subseq_len = 0
                for j in a:
                    if i % j == 0:
                        if LCM == 0:
                            LCM = j
                        else:
                            LCM = lcm(LCM, j)
                        subseq_len += 1
                if LCM == i:
                    mx_len = max(mx_len, subseq_len)
            
            subseq_len = 0
            q = mx // i
            if q not in set_a:
                LCM = 0
                for j in a:
                    if q % j == 0:
                        if LCM == 0:
                            LCM = j
                        else:
                            LCM = lcm(LCM, j)
                        subseq_len += 1
                if LCM == q:
                    mx_len = max(mx_len, subseq_len)

    yield mx_len
    return

def test():
    ans = []
    for _ in range(inp()):
        for a in solve():
            ans.append(a)
    for i in ans:
        print(i)

def submit():
    for _ in range(inp()):
        for a in solve():
            print(a)

submit()