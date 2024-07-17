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
    n = inp()
    s = insr()
    if n == 2:
        yield int(s[0] + s[1])
        return
    
    if n == 3:
        if int(s[0]) == 0 or int(s[2]) == 0:
            yield 0
            return

    if n > 3:
        for x in s:
            if int(x) == 0:
                yield 0
                return

    mn = float('inf')
    for i in range(n - 1):
        arr = list(s)
        arr[i] = s[i] + s[i + 1]
        arr[i + 1] = s[i] + s[i + 1]
        sm = 0
        for j in range(n):
            if j == i + 1:
                continue
            sm += int(arr[j])
        ones = 0
        for j in range(n):
            if j == i + 1:
                continue
            if int(arr[j]) == 1:
                ones += 1
            else:
                sm -= ones
                ones = 0
        sm -= ones
        if ones == n - 1:
            sm += 1
        mn = min(mn, sm)
    
    yield mn
                

        
       
                
        


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

test()