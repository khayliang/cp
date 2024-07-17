import sys
from collections import deque, defaultdict
import random

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


"""
low: inclusive
high: exclusive

if fails, index returned will be the index of the
next smallest value to x
"""
def binary_search(arr, l, h, x):
    m = 0
 
    while l < h:
        m = (h + l) // 2
        
        if (arr[m] == x):
            return (True, m)
 
        if arr[m] < x:
            l = m + 1
        else:
            h = m

    if arr[m] > x:
        m -= 1
            
    return (False, m)

def solver(k, a, b, d):
    print(f"k: {k}, a: {a}, b: {b}, d: {d}")
    if d< a[0]:
        return int(d / (a[0] / b[0]))
    found, i = binary_search(a, 0, len(a), d)
    if found:
        return b[i]
    else:
        return int(((d - a[i]) * (b[i + 1] - b[i]))/ (a[i + 1] - a[i]) + b[i])


# use yield to give ans. return to stop
def solve():
    n, k, q = inlt()
    a = inlt()
    b = inlt()

    res = []

    for _ in range(q):
        d = inp()
        if d < a[0]:
            res.append((d *  b[0]) // a[0])
            continue
        found, i = binary_search(a, 0, len(a), d)
        if found:
            res.append(b[i])
        else:
            res.append(((d - a[i]) * (b[i + 1] - b[i]))// (a[i + 1] - a[i]) + b[i])
    
    yield outlt(res)

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

"""
if __name__ == "__main__":
    while True:
        k = random.randint(5, 20)
        a = [7]
        b = [5]
        for i in range(k - 1):
            a.append(a[-1] + random.randint(1, 20))
            b.append(b[-1] + random.randint(1, 20))
            n = a[-1]

        for j in range(20):
            q = random.randint(7, n)
            print(solver(k, a, b, q))
"""
test()