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

############ ---- Output Functions ---- ############
def outlt(a):
    return " ".join(map(str, a))

def get_prefix_sum(a):
    a_sm = [0]

    for x in a:
        a_sm.append(a[-1] + x)

    return a_sm

def window(a_pf, b_pf, c_pf):
    mx = 0
    prev = 0
    l = 1

    # inclusive
    for r in range(1, n):
        while l != r:
            a_sm = a_pf[r + 1] - a_pf[l]
            bc_sm = b_pf[l] + c_pf[-1] - c_pf[r + 1]
            cb_sm = c_pf[l] + b_pf[-1] - b_pf[r + 1]

            if a_sm + bc_sm < 



# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()
    b = inlt()
    c = inlt()

    a_sm = get_prefix_sum(a)
    b_sm = get_prefix_sum(b)
    c_sm = get_prefix_sum(c)

    mx = 0

   

        

        


        


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