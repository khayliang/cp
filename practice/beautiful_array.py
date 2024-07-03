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
    n, k = inlt()
    a = inlt()
    removed = [False for _ in range(n)]
    a.sort()

    for i, x in enumerate(a[:-1]):
        if removed[i]:
            continue
        
        if x == a[i + 1]:
            removed[i] = True
            removed[i + 1] = True

    d = {}
    for i, x in enumerate(a):
        if removed[i] == True:
            continue

        r = x % k
        if r in d:
            y = d[r][0]
            d[r].append(x)
        else:
            d[r] = deque([x])
    
    amt = 0
    odds = 0
    for _, q in d.items():
        if len(q) % 2 == 1:
            odds += 1
            even_arr = [0]
            odd_arr = [0]
            j = 0
            while len(q) > 1:
                q_i = abs(q.popleft() - q[0]) // k
                if j % 2 == 0:
                    even_arr.append(q_i + even_arr[-1])
                else:
                    odd_arr.append(q_i + odd_arr[-1])
                j += 1
            
            mn = float('inf')
            for j in range(len(even_arr)):
                curr = even_arr[j] + odd_arr[-1] - odd_arr[j]
                mn = min(mn, curr)

            amt += mn
        else:
            while q:
                amt += (q.pop() - q.pop()) // k

    if odds == 0 or odds == 1:
        yield amt
    else:
        yield -1

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