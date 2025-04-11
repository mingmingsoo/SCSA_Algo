from collections import defaultdict, deque

m = int(input())
n = int(input())
grid = [list(map(int, input())) for i in range(n)]
visited = [[0] * m for i in range(n)]
num = 1

shape_dict = defaultdict(list)
row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]


def rotation(small):
    sn, sm = len(small), len(small[0])
    ro = [[0] * sn for i in range(sm)]
    for i in range(sm):
        for j in range(sn):
            ro[i][j] = small[sn - j - 1][i]
    return ro


def bfs(sr, sc):
    global num
    location = []
    q = deque([(sr, sc)])
    minr, maxr, minc, maxc = sr, sr, sc, sc
    while q:
        r, c = q.popleft()
        location.append((r, c))
        minr = min(r, minr)
        minc = min(c, minc)
        maxr = max(r, maxr)
        maxc = max(c, maxc)

        for k in range(8):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or not grid[nr][nc] or visited[nr][nc]:
                continue
            visited[nr][nc] = num
            q.append((nr, nc))
    small = [[0] * (maxc - minc + 1) for i in range(maxr - minr + 1)]
    for lr, lc in location:
        small[lr-minr][lc-minc] = 1

    same = False
    for k, v in shape_dict.items():
        for s in v:
            if s == small:
                same = True
                for r, c in location:
                    visited[r][c] = k
                break
        if same:
            num -= 1
            break
    if not same:
        shape_dict[num].append(small)
        small_zip = list(map(list, zip(*small)))
        small_zip_T = list(reversed(small_zip))
        small_zip = list(map(list, zip(*small_zip_T)))
        shape_dict[num].append(small_zip)

        small = rotation(small)
        shape_dict[num].append(small)
        small_zip = list(map(list, zip(*small)))
        small_zip_T = list(reversed(small_zip))
        small_zip = list(map(list, zip(*small_zip_T)))
        shape_dict[num].append(small_zip)

        small = rotation(small)
        shape_dict[num].append(small)
        small_zip = list(map(list, zip(*small)))
        small_zip_T = list(reversed(small_zip))
        small_zip = list(map(list, zip(*small_zip_T)))
        shape_dict[num].append(small_zip)

        small = rotation(small)
        shape_dict[num].append(small)
        small_zip = list(map(list, zip(*small)))
        small_zip_T = list(reversed(small_zip))
        small_zip = list(map(list, zip(*small_zip_T)))
        shape_dict[num].append(small_zip)


for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = num
            bfs(i, j)
            num += 1
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            print(chr(visited[i][j] + 96), end="")
        else:
            print(0, end="")
    print()
