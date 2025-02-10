'''
풀이시간 30분
스터디 과제일줄 오르고
제출기록에 정우님있어서 풀었습니다...헤헿ㅎ

3 3
1
1 0
1 1
4 3 2 1
반례

틀렸던 이유: 습관처럼 d = (d+1)%4 를 했는데
d를 바꿔주는 것이 아닌 d의 idx를 바꿔줘야함.

'''
n,m = map(int,input().split())

grid = [[0]*m for i in range(n)]
x = int(input())
for i in range(x):
    r,c = map(int,input().split())
    grid[r][c] = -1 # 장애물 처리
r , c = map(int,input().split())
grid[r][c] = 1 #  로봇 처음 위치
dir = list(map(lambda x: int(x)-1,input().split()))
row = [-1,1,0,0]
col = [0,0,-1,1]

def go():
    global r,c
    # 지정된 방향으로 움직일 수 있는 만큼 움직임
    # 벽 or 방문한 지역or 장애물 만나면 방향을 틀음

    didx = 0
    d = dir[didx]
    cnt = 0
    while True:

        nr = r+row[d]
        nc = c+col[d]
        if(0<=nr<n and 0<=nc<m and grid[nr][nc]==0):
            grid[nr][nc] = grid[r][c]+1
            r = nr
            c = nc
            cnt = 0
        else:
            didx = (didx+1)%4
            d = dir[didx]
            cnt +=1
            # print(d)
            if(cnt>4):
                break

go()
print(r,c)


