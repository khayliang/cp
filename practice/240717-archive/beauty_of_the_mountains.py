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

def prefix_sum(n, m, matrix):
    res = [[0 for j in range(m)] for i in range(n)]
    res[0][0] = matrix[0][0]
    for i in range(1, n):
        res[i][0] = res[i - 1][0] + matrix[i][0]
    for i in range(1, m):
        res[0][i] = res[0][i - 1] + matrix[0][i]
    
    for i in range(1, n):
        for j in range(1, m):
            res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + matrix[i][j]

    return res
    
def sliding_window_gcd(n, m, matrix, window_size, diff):
    div = 0
    prefix_mat = prefix_sum(n, m, matrix)
    for x in range(n - window_size + 1):
        for y in range(m - window_size + 1):
            sm = prefix_mat[x + window_size - 1][y + window_size - 1]
            if x > 0:
                sm -= prefix_mat[x - 1][y + window_size - 1]
            if y > 0:
                sm -= prefix_mat[x + window_size - 1][y- 1]
            if x > 0 and y > 0:
                sm += prefix_mat[x - 1][y - 1]

            rs = window_size ** 2 - (2 * sm)
            if div == 0:
                div = rs
            else:
                div = math.gcd(div, rs)
            if div != 0 and diff % div == 0:
                return div
    return div

# use yield to give ans. return to stop
def solve():
    n, m, k = inlt()
    a = []
    tp = []
    for _ in range(n):
        a.append(inlt())
    for _ in range(n):
        tp.append(list(map(int, insr())))
    s = 0
    si = 0
    for i in range(n):
        for j in range(m):
            if tp[i][j] == 0:
                s += a[i][j]
            else:
                si += a[i][j]
    
    if s - si == 0:
        yield "YES"
        return
    
    div = sliding_window_gcd(n, m, tp, k, s - si)
    if div == 0:
        yield "NO"
        return

    # print(f"div: {div} s - si: {s - si}")
    if (si - s) % div == 0:
        yield "YES"
    else:
        yield "NO"

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