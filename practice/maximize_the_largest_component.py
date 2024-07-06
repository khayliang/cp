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

# use yield to give ans. return to stop
def solve():
    n, m = inlt()
    grid = [insr() for _ in range(n)]

    # dfs to get components
    visited = [[-1 for i in range(m)] for i in range(n)]
    size = []
    s = deque()
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" and visited[i][j] == -1:
                visited[i][j] = count
                s.append((i, j))
            
            curr_size = 0
            while s:
                x, y = s.pop()
                curr_size += 1
                if x > 0 and grid[x - 1][y] == "#" and visited[x - 1][y] == -1:
                    visited[x - 1][y] = count
                    s.append((x - 1, y))
                if x < n - 1 and grid[x + 1][y] == "#" and visited[x + 1][y] == -1:
                    visited[x + 1][y] = count
                    s.append((x + 1, y))
                if y > 0 and grid[x][y - 1] == "#" and visited[x][y - 1] == -1:
                    visited[x][y - 1] = count
                    s.append((x, y - 1))
                if y < m - 1 and grid[x][y + 1] == "#" and visited[x][y + 1] == -1:
                    visited[x][y + 1] = count
                    s.append((x, y + 1))
            
            if curr_size > 0:
                count += 1
                size.append(curr_size)

    max_amt = 0
    for i in range(n):
        amt = 0
        contains = set()
        for j in range(m):
            item = visited[i][j]
            if item == -1:
                amt += 1
                if i > 0 and visited[i - 1][j] != -1 and visited[i - 1][j] not in contains:
                    contains.add(visited[i - 1][j])
                    amt += size[visited[i - 1][j]]
                if i < n - 1 and visited[i + 1][j] != -1 and visited[i + 1][j] not in contains:
                    contains.add(visited[i + 1][j])
                    amt += size[visited[i + 1][j]]
                if j > 0 and visited[i][j - 1] != -1 and visited[i][j - 1] not in contains:
                    contains.add(visited[i][j - 1])
                    amt += size[visited[i][j - 1]]
                if j < m - 1 and visited[i][j + 1] != -1 and visited[i][j + 1] not in contains:
                    contains.add(visited[i][j + 1])
                    amt += size[visited[i][j + 1]]
            else:
                if item not in contains:
                    contains.add(item)
                    amt += size[item]
        max_amt = max(max_amt, amt)
    
    for j in range(m):
        amt = 0
        contains = set()
        for i in range(n):
            item = visited[i][j]
            if item == -1:
                amt += 1
                if i > 0 and visited[i - 1][j] != -1 and visited[i - 1][j] not in contains:
                    contains.add(visited[i - 1][j])
                    amt += size[visited[i - 1][j]]
                if i < n - 1 and visited[i + 1][j] != -1 and visited[i + 1][j] not in contains:
                    contains.add(visited[i + 1][j])
                    amt += size[visited[i + 1][j]]
                if j > 0 and visited[i][j - 1] != -1 and visited[i][j - 1] not in contains:
                    contains.add(visited[i][j - 1])
                    amt += size[visited[i][j - 1]]
                if j < m - 1 and visited[i][j + 1] != -1 and visited[i][j + 1] not in contains:
                    contains.add(visited[i][j + 1])
                    amt += size[visited[i][j + 1]]
            else:
                if item not in contains:
                    contains.add(item)
                    amt += size[item]
        max_amt = max(max_amt, amt)
    
    yield max_amt
            

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