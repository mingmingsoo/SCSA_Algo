from collections import deque

n = int(input())
grid = [list(input()) for i in range(n)]


gridNoColor = [[0]*n for i in range(n)]
for i in range(0,n):
    for j in range(0,n):
        if(grid[i][j]!="G"):
            gridNoColor[i][j] = grid[i][j]
        else:
            gridNoColor[i][j] = 'R'


row = [-1,1,0,0]
col = [0,0,1,-1]
def bfsColor(i, j, arr, color):
    global visited
    q = deque()
    q.append((i,j))
    visited.add((i,j))

    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and arr[nr][nc] == color):
                q.append((nr, nc))
                visited.add((nr, nc))


def ColorCount(arr):
    total = 0
    for i in range(n):
        for j in range(n):
            if ((i, j) not in visited):
                bfsColor(i, j, arr, arr[i][j])
                total += 1
    return total



visited = set()
yes = ColorCount(grid)

visited = set()
no = ColorCount(gridNoColor)


print(yes, no)