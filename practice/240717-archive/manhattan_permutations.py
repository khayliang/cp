import sys
from collections import deque, defaultdict
from itertools import permutations
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

def solve_test(n, k):import sys
from collections import deque, defaultdict
from itertools import permutations

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

    if k % 2 != 0 or k >= (n * (n + 1)) // 2:
        yield "NO"
        return
    
    d = {}

    for i in range(1, k + 1):
        print(k)
        if k >= 2 * (n - 2 * i + 1):
            d[i] = n - i + 1
            d[n - i + 1] = i
            k -= 2 * (n - 2 * i + 1)
            if k == 0:
                break
        elif k > 0:
            x = max(abs(k // 2 + i), abs(i - k // 2))
            d[x] = i
            d[i] = x
            k -= 2 * abs(i - x)
            break
        else:
            break
    
    if k != 0:
        yield "NO"
        return

    res = []
    for i in range(1, n + 1):
        if i in d:
            res.append(d[i])
        else:
            res.append(i)
    
    yield "YES"
    yield outlt(res)


# use yield to give ans. return to stop
def solve():
    n, k = inlt()

    if k % 2 != 0 or k >= (n * (n + 1)) // 2:
        yield "NO"
        return
    
    d = {}

    for i in range(1, k + 1):
        if k >= 2 * (n - 2 * i + 1):
            d[i] = n - i + 1
            d[n - i + 1] = i
            k -= 2 * (n - 2 * i + 1)
            if k == 0:
                break
        elif k > 0:
            x = max(abs(k // 2 + i), abs(i - k // 2))
            d[x] = i
            d[i] = x
            k -= 2 * abs(i - x)
            break
        else:
            break
    
    if k != 0:
        yield "NO"
        return

    res = []
    for i in range(1, n + 1):
        if i in d:
            res.append(d[i])
        else:
            res.append(i)
    
    yield "YES"
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

def brute_test():
    while True:
        n = random.randint(1, 8)
        k = random.randint(0, 42)
        res = list(solve_test(n, k))
        if len(res) != 1:
            a = map(int, res[1].split(' '))
            sm = 0
            for i, x in enumerate(a):
                i += 1
                sm += abs(x - i)
            if sm != k:
                print(n, k)
                print(a)
                print(sm)
                break

test()
#test()