import sys
'''
각 열마다 모두 한칸 내려갈 수 있으면
전부 내려가고
하나라도 내려갈 수 없으면 stop
'''
n,m = map(int, sys.stdin.readline().split())

grid = [list(sys.stdin.readline()) for i in range(n)]

diff = 5000
for j in range(m):
    start = -1
    end = -1
    for i in range(n - 1, -1, -1):
        if (grid[i][j] == '#'):
            start = i-1
        if (grid[i][j] == 'X'):
            end = max(i, end)
    if(start != -1 and end != -1):
        diff = min(diff, start- end)

for j in range(m):
    start = 5000
    end = -1
    isDown = False
    for i in range(n):
        if (grid[i][j] == 'X'):
            isDown = True
            start = min(start,i)
            end = max(end,i)

    if(isDown and start != 5000 and end != -1):
        for i in range(end+diff, start+diff -1, -1 ):
            grid[i][j] = grid[i-diff][j]
        for i in range(start, start+diff): # 0 1
            grid[i][j]= '.'


for i in range(n):
    for j in range(m):
        print(grid[i][j], end = "")
    print()
