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

def binary_search(arr, l, h, x):
    m = 0
 
    while l < h:
        m = (h + l) // 2
        
        if (arr[m] == x):
            return (True, m)
 
        if arr[m] < x:
            l = m + 1
        else:
            h = m
            
    return (False, m)

for _ in range(inp()):
    a, b, n, m = inlt()
    chips = []
    for _ in range(n):
        chips.append(inlt())
    
    x_arr = [[] for _ in range(a)]
    y_arr = [[] for _ in range(b)]

    chips.sort(key=lambda x: x[1])
    for chip in chips:
        x_arr[chip[0] - 1].append(chip[1] - 1)
    
    chips.sort(key=lambda x: x[0])
    for chip in chips:
        y_arr[chip[1] - 1].append(chip[0] - 1)
    
    u = 0
    d = a

    l = 0
    r = b

    amt_a = 0
    amt_b = 0

    for move in range(m):
        c, _, k = insr()
        k = int(k)

        if c == 'U':
            for i in range(u, u + k):
                u += 1
                found_l ,l_i = binary_search(x_arr[i], 0, len(x_arr[i]), l)
                found_r, r_i = binary_search(x_arr[i], 0, len(x_arr[i]), r - 1)
                
                r_i += 1
                
                if move % 2 == 0:
                    amt_a += r_i - l_i
                else:
                    amt_b += r_i - l_i

        elif c == 'D':
            for i in range(d - k, d):
                d -= 1
                found_l ,l_i = binary_search(x_arr[i], 0, len(x_arr[i]), l)
                found_r, r_i = binary_search(x_arr[i], 0, len(x_arr[i]), r - 1)

                r_i += 1
                
                if move % 2 == 0:
                    amt_a += r_i - l_i
                else:
                    amt_b += r_i - l_i

        elif c == 'L':
            for i in range(l, l + k):
                l += 1
                found_u ,u_i = binary_search(y_arr[i], 0, len(y_arr[i]), u)
                found_d, d_i = binary_search(y_arr[i], 0, len(y_arr[i]), d - 1)

                d_i += 1
                
                if move % 2 == 0:
                    amt_a += d_i - u_i
                else:
                    amt_b += d_i - u_i

        elif c == 'R':
            for i in range(r - k, r):
                r -= 1
                found_u ,u_i = binary_search(y_arr[i], 0, len(y_arr[i]), u)
                found_d, d_i = binary_search(y_arr[i], 0, len(y_arr[i]), d - 1)

                d_i += 1
                
                if move % 2 == 0:
                    amt_a += d_i - u_i
                else:
                    amt_b += d_i - u_i
    print(amt_a, amt_b)
