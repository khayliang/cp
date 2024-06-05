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
    n, f, k = inlt()
    a = inlt()

    fav_no = a[f - 1]

    fav_no_count = 0
    for i in a:
        if i == fav_no:
            fav_no_count += 1

    a.sort(reverse=True)

    if k == n:
        print("YES")
        continue

    k_val = a[k - 1]

    if fav_no > k_val:
        print("YES")
    elif fav_no == k_val and fav_no_count == 1:
        print("YES")
    elif fav_no == k_val and fav_no_count > 1:
        if a[k] != fav_no:
            print("YES")
        else:
            print("MAYBE")
    else:
        print("NO")