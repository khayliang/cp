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
    n, m = inlt()
    grid = [insr() for _ in range(n)]
    # left
    hashes = []
    for x, row in enumerate(grid):
        for y, c in enumerate(row):
            if c == "#":
                hashes.append((x, y))
    hashes.sort(key=lambda x: x[0])
    top_x = hashes[0][0]
    bot_x = hashes[-1][0]

    hashes.sort(key=lambda x: x[1])
    left_y = hashes[0][1]
    right_y = hashes[-1][1]

    x = ((bot_x + top_x) // 2) + 1
    y = ((right_y + left_y) // 2) + 1

    yield f'{x} {y}'




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