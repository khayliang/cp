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

def bitstr(bitset):
    return [i > 0 for i in bitset]


def is_valid(arr, k, max_val):
    bitset = [0] * max_val.bit_length()

    for i in range(k):
        curr = arr[i]
        for j in range(max_val.bit_length()):
            if curr & (1 << j):
                bitset[j] += 1


    for i in range(0, n - k):
        old = arr[i]
        new = arr[i + k]

        prev = bitstr(bitset)
        
        for j in range(max_val.bit_length()):
            if old & (1 << j):
                bitset[j] -= 1
            if new & (1 << j):
                bitset[j] += 1

        
        curr = bitstr(bitset)

        if curr != prev:
            return False
    return True

for _ in range(inp()):
    n = inp()
    a = inlt()
    max_val = max(a)
    l = 1
    h = len(a)
    prev_valid = len(a)
    while l < h:
        m = (h + l) // 2
        
        if (is_valid(a, m, max_val)):
            h = m
            prev_valid = m
        else:
            l = m + 1
             
    print(prev_valid)