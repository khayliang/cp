"""
low: inclusive
high: exclusive

if fails, index returned will be the index of the
next smallest value to x
"""

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

    if arr[m] > x:
        m -= 1
            
    return (False, m)

if __name__ == "__main__":
    print(binary_search([0,3,5,7,9], 0, 5, 8))