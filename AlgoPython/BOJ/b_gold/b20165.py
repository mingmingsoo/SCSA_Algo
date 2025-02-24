'''
문제설명
    도미노는 넘어질 때 본인 높이만큼만 넘어뜨릴 수 있음
입력
    맵, 라운드 횟수
    E, W, S, N  동, 서, 남, 북

출력
    최종 상태와 공격수의 점수
    F는 넘어짐 S는 넘어지지 않음

구상
    서있고, 쓰러져있는 정보를 관리하는 state 변수를 이용.
'''
from collections import deque

n,m,game_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
state = [["S"]* m for i in range(n)] # S 면 서있음

row = [0,0,1,-1]
col = [1,-1,0,0]

ans = 0
def fall(r,c,d):
    global ans
    height = grid[r][c] # 쓰러뜰일 수 있는 길이
    possible = deque([(r,c,height)])
    while possible:
        r,c,height = possible.popleft()
        if(state[r][c]=="S"):
            ans+=1
            state[r][c] = "F"

        for h in range(1,height):
            nr = r+row[d]*h
            nc = c+col[d]*h
            if not (0<=nr<n and 0<=nc<m):
                continue
            if state[nr][nc] =="S":
                possible.append((nr,nc,grid[nr][nc]))


for gn in range(game_num):
    r,c,dir = input().split()
    r,c = int(r)-1, int(c)-1
    d = "EWSN".index(dir)

    fall(r,c,d)

    # 세워..
    r,c = map(lambda x:int(x)-1, input().split())
    state[r][c] = "S"

print(ans)
for _ in state:
    print(*_)