import sys

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

ans = 0
visited = [[0] * m for i in range(n)]
row = [-1, 0, 1]
col = [1, 1, 1]
'''
반례
5 5
xxx..
xxx..
xxx..
...x.
...x.
정답1

5 5
.xx.x
..x.x
....x
...x.
...x.
정답1

3 3
x..
x.x
x.x
정답0
'''
for idx in range(n):
    if grid[idx][0] != ".":
        continue
    r, c = idx, 0
    while True:
        if c == m-1:
            ans+=1
            break
        is_go = False
        for k in range(3):
            nr = r+row[k]
            nc = c+col[k]
            if not(0<=nr<n and 0<=nc<m) or grid[nr][nc] !="." or visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            is_go = True
            r,c = nr,nc
            break
        if not is_go:
            break
    # print("--------------")
    # for _ in visited:
    #     print(*_)




print(ans)
