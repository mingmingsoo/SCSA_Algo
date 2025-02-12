'''
[문제 설명]
    칠공주의 규칙
    1. 7명의 여학생들로 구성
    2. 7명의 자리는 가로나 세로로 인접
    3. 이다솜파만 있어도 되는 것은 아니다.
    4. 7명 중 4명 이상은 이다솜파
    소문난 칠공주가 앉을 수 있는 모든 경우의 수 구하라

[입력]
    행렬은 모두 5*5
    이다솜파 S, 임도연파 Y
[출력]
    경우의 수
[구상]
    조합으로 가능한 모든 7개의 점을 구하고
    Y가 4 개이상이면 탈출.
    탈출이 안됐으면
    그 점이 연결되어있는가 bfs확인한다.
'''
from collections import deque

grid = [list(input()) for i in range(5)]
ans = 0

row = [-1,1,0,0]
col = [0,0,1,-1]

arr = list(range(25))
sel = [0]*7


def bfs(grid, r, c):
    # 정점이 연결된게 7개면 true
    edge = 0
    visited = [[False]*5 for i in range(5)]
    visited[r][c] = True
    q = deque([(r,c)])

    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r+row[k]
            nc = c+col[k]
            if(not(0<=nr<5 and 0<=nc<5)):
                continue
            if(not visited[nr][nc] and grid[nr][nc] == 1):
                visited[nr][nc] = True
                q.append((nr,nc))
                edge+=1
    if(edge>=6):
        return True
    else:
        return False

def combi(sidx,idx): # Y가 4개이상이면 return
    global ans
    if(sidx==7):
        # print(sel)
        # 얘네중 이다솜이 4명이상이고 bfs로 연결되어있으면 ans +=1
        Y = 0
        for num in sel:
            r, c = num//5, num%5
            if(grid[r][c]=="Y"):
                Y+=1
                if(Y>=4):
                    return
        check = [[0]*5 for i in range(5)]
        for num in sel:
            r, c = num//5, num%5
            check[r][c] = 1
        # for xx in check:
        #     print(xx)
        if(bfs(check,sel[0]//5, sel[0]%5)):
            ans+=1
            return
        return
    if(idx==25):
        return

    sel[sidx] = arr[idx]
    combi(sidx+1, idx+1)
    combi(sidx, idx+1)




combi(0,0)


print(ans)