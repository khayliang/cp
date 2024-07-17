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

"""
low: inclusive
high: exclusive

if fails, index returned will be the index of the
next smallest value to x
"""
def binary_search(n):
    if n == 1:
        return 1
    m = 0
    l = 0
    h = n
    while l < h:
        m = (h + l) // 2

        e = 0
        if m % 2 != 0:
            e = (m * (m + 1)) / 2
        else:
            e = ((m * m) / 2) + 1

        v = e + 1

        if v < n:
            l = m + 1
        else:
            h = m
            
    return h


def gen_primes(m):
    n = 17389
    prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    prime_numbers = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_numbers.append(p)
        if len(prime_numbers) == m:
            break
    return prime_numbers


def dfs(graph, visited, stk, prime, x):
    rec_stk = deque([x])
    path = deque([])

    while graph[x]:
        p, i = graph[x].pop()
        if visited[i]:
            continue
        visited[i] = True
        dfs(graph, visited, stk, prime, p)
    stk.append(prime[x])


# use yield to give ans. return to stop
def solve():
    n = inp()

    if n == 2:
        yield [2, 2]
        return

    m = binary_search(n)
    primes = gen_primes(m)

    path = deque([])
    reverse_path = deque([])

    graph = [deque([]) for _ in range(m)]

    total = 0
    for i in range(0, m):
        for j in range(i, m):
            if m % 2 == 0 and (i + 1) % 2 == 0 and i + 1 == j:
                continue
            graph[i].append((j, total))
            graph[j].append((i, total))
            total += 1
    
    visited = [False] * (total + 1)

    stk = deque([])
    dfs(graph, visited, stk, primes, 0)
    yield list(stk)[0:n]

def test():
    ans = []
    for _ in range(inp()):
        for a in solve():
            ans.append(a)
    for i in ans:
        print(*i)

def submit():
    for _ in range(inp()):
        for a in solve():
            print(*a)

submit()