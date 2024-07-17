import sys
from collections import deque, defaultdict
from itertools import permutations
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

############ ---- Output Functions ---- ############
def outlt(a):
    return " ".join(map(str, a))

# use yield to give ans. return to stop
def solve():
    n = inp()
    sn = str(n)
    l = int(math.log10(n)) + 1
    amt = 0
    res_arr = []
    for a in range(1, 10001):
        for b in range(l * a - 6, l * a):
            if b < 1:
                continue
            if l * a - b == int(math.log10(n * a - b)) + 1:
                res = n * a - b

                if res == 0:
                    if l * a - b == 0:
                        amt += 1
                    continue
        
                sr = "".join([sn] * ((l * a - b) // l)) + sn[:((l * a - b) % l) + 1]
                resr = str(res)
                good = True
                for i in range(l * a - b):
                    if sr[i] != resr[i]:
                        good = False
                        break
                if good:
                    res_arr.append(f"{a} {b}")
                    amt += 1
            
    yield amt
    for s in res_arr:
        yield s
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