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


def dist(r, h):
    return abs(r[0]-h[0]) + abs(r[1]-h[1])

for _ in range(inp()):
    n = inp()
    s = insr()

    x = 0
    y = 0

    for ch in s:
        if ch == 'N':
            y += 1
        elif ch == 'S':
            y -= 1
        elif ch == 'E':
            x += 1
        elif ch == 'W':
            x -= 1
    
    if x % 2 != 0 or y % 2 != 0:
        print("NO")
        continue

    if len(s) == 2 and x == 0 and y == 0:
        print("NO")
        continue

    if x == 0 and y == 0:
        res = "R"
        finished = False
        for ch in s[1:]:
            if not finished:
                if ch == 'N' and s[0] == "S":
                    res += "R"
                    finished = True
                elif ch == 'S' and s[0] == "N":
                    res += "R"
                    finished = True
                elif ch == 'E' and s[0] == "W":
                    res += "R"
                    finished = True
                elif ch == 'W' and s[0] == "E":
                    res += "R"
                    finished = True
                else:
                    res += "H"
            else:
                res += "H"
        print(res)
        continue
    
    dest_x = x / 2
    dest_y = y / 2

    r_x = 0
    r_y = 0
    res = ["H" for _ in range(n)]

    for i, ch in enumerate(s):
        if ch == 'N' and r_y < dest_y:
            r_y += 1
            res[i] = "R"
        elif ch == 'S' and r_y > dest_y:
            r_y -= 1
            res[i] = "R"
        elif ch == 'E' and r_x < dest_x:
            r_x += 1
            res[i] = "R"
        elif ch == 'W' and r_x > dest_x:
            r_x -= 1
            res[i] = "R"
        

        
        if r_x == dest_x and r_y == dest_y:
            break
    
    print("".join(res))
    





    