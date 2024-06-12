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

# use yield to give ans. return to stop
def solve(): 
    x, y, z, k = inlt()

    a = [('x', x), ('y', y), ('z', z)]
    a.sort(key=lambda x: x[1])

    d = {'x': 0, 'y': 0, 'z': 0}

    v = x * y * z
    for c, i in a:
        prop = k / v
        d[c] = i * prop
        v = v / i

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