import sys

'''
bfs인데 지금까지 알파벳이 뭐였는지 달고 다님.
-> 시간초는 널널한데 메모리초과인거 보면 dfs인가?
'''

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [[0] * m for i in range(n)]

for i in range(n):
    tmp = list(input())
    for j in range(m):
        grid[i][j] = ord(tmp[j]) - 65
        # grid[i][j] = tmp[j]
ans = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

def dfs(r, c, cnt, aset):
    global ans
    ans = max(cnt, ans)

    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]
        if (not (0 <= nr < n and 0 <= nc < m)):
            continue
        if (grid[nr][nc] not in aset):
            aset.append(grid[nr][nc])
            dfs(nr, nc, cnt + 1, aset)
            aset.pop()  # 그리고 pop 해줘야 다음 방향에 영향이 없음


dfs(0, 0, 1, [grid[0][0]])

print(ans)



# def bfs(i, j, a):
#     global ans
#     alphaTmp = [a] # 지금까지 나온 알파벳
#     q = deque([(i,j,1,alphaTmp)])
#
#     while q:
#         r,c,cnt,aset = q.popleft()
#         ans = max(cnt,ans)
#
#         for k in range(4):
#             nr = r+row[k]
#             nc = c+col[k]
#             if(not(0<=nr<n and 0<=nc<m)):
#                 continue
#             if(grid[nr][nc] not in aset):
#                 aset.append(grid[nr][nc])
#                 q.append((nr,nc,cnt+1,aset[:])) # 복사본을 넣어줘야 변화가 안생김
#                 aset.pop() # 그리고 pop 해줘야 다음 방향에 영향이 없음
#
#
#
# bfs(0,0,grid[0][0]) # 시작점과 그 알파벳