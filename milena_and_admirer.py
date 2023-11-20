import sys
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

# return no. of steps and the end value
def break_amt(x, k):
    if x - (x // 2) <= k:
        return (1, x//2)

    rem = x % k
    if rem == 0:
        return ((x // k) - 1, k)
    
    amt = x // k
    to_break = rem + k
    return (amt, to_break // 2)

def sol(l):
    count = 0
    no_to_hit = l[-1]

    for i in reversed(range(len(l))):
        if l[i] > no_to_hit:

            amt, no_to_hit = break_amt(l[i], no_to_hit)
            count += amt
        else:
            no_to_hit = l[i]
    
    return count

cases = inp()

for _ in range(cases):
    n = inp()
    l = inlt()
    print(sol(l))