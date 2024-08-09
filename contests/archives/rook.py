import sys
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

cases = inp()
for _ in range(cases):
    pos = insr()
    for i in range(8):
        ch = chr(ord('a') + i)
        if ch == pos[0]:
            continue
        print(ch + pos[1])
    for i in range(1, 9):
        if i == int(pos[1]):
            continue
        print(pos[0] + str(i))

