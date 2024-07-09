import sys
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

def outmat(mat):
    res = ""
    for x in mat:
        res += outlt(x) + "\n"
    return res


# use yield to give ans. return to stop
def solve():
    n, m = inlt()
    mat = [inlt() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            val = mat[i][j]
            mx = 0

            if i > 0:
                if val > mat[i - 1][j]:
                    mx = max(mx, mat[i - 1][j])
                else:
                    continue
            if i < n - 1:
                if val > mat[i + 1][j]:
                    mx = max(mx, mat[i + 1][j])
                else:
                    continue
            if j > 0:
                if val > mat[i][j - 1]:
                    mx = max(mx, mat[i][j - 1])
                else:
                    continue
            if j < m - 1:
                if val > mat[i][j + 1]:
                    mx = max(mx, mat[i][j + 1])
                else:
                    continue

            mat[i][j] = mx
    yield outmat(mat)
            
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