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

for _ in range(inp()):
    n, k = inlt()
    s = input()
    ans1 = 0
    for i in range(n):
        ans1 = ans1 << 1
        if (i // k) % 2 == 0:
            ans1 += 1
    ans2 = (pow(2, n) - 1) ^ ans1
    
    found = False
    new_s = int(s, 2)
    if new_s == ans1 or new_s == ans2:
        print(n)
        continue

    for i in range(n):
        new_s = f'{s[i + 1:n]}{s[i::-1]}'
        new_s = int(new_s, 2)
        if new_s == ans1 or new_s == ans2:
            print(i + 1)
            found = True
            break
    
    if not found:
        print(-1)
