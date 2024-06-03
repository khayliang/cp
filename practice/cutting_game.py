def solve(tc):
    a, b, n, m = map(int, input().split())
    ver, hor = [], []
    for i in range(n):
        x, y = map(int, input().split())
        ver.append((x, y))
        hor.append((y, x))
    deleted = set()
    hor.sort()
    ver.sort()
    ans = [0, 0]
    u, d = 1, a
    l, r = 1, b
    hl, hr = 0, n - 1
    vl, vr = 0, n - 1
    for i in range(m):
        c, k = input().split()
        k = int(k)
        if c == 'U':
            u += k
            while vl <= vr and ver[vl][0] < u:
                if ver[vl] not in deleted:
                    ans[i % 2] += 1
                    deleted.add(ver[vl])
                vl += 1
        if c == 'D':
            d -= k
            while vl <= vr and ver[vr][0] > d:
                if ver[vr] not in deleted:
                    ans[i % 2] += 1
                    deleted.add(ver[vr])
                vr -= 1
        if c == 'L':
            l += k
            while hl <= hr and hor[hl][0] < l:
                if (hor[hl][1], hor[hl][0]) not in deleted:
                    ans[i % 2] += 1
                    deleted.add((hor[hl][1], hor[hl][0]))
                hl += 1
        if c == 'R':
            r -= k
            while hl <= hr and hor[hr][0] > r:
                if (hor[hr][1], hor[hr][0]) not in deleted:
                    ans[i % 2] += 1
                    deleted.add((hor[hr][1], hor[hr][0]))
                hr -= 1
    print(ans[0], ans[1])


t = int(input())
for i in range(1, t + 1):
    solve(i)