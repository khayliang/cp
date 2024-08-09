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
    x, y = inlt()
    n = 10
    z = x ^ y
    # Finding the highest differing bit position
    max_length = 0
    
    # The length of the longest common subsegment is determined by the highest bit position of 1 in z
    while z > 0:
        max_length += 1
        z >>= 1
    
    # There might be a tail of zeros at the end
    print(max_length)