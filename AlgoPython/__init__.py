#B17370
"""
시도횟수 : 2회 (방향 delta 잘못 씀)
실행시간 : 464ms
메모리 : 112084KB

[Refactoring]
- N<=4일 때는 탐색이 멈출 리가 없다..!(감사합니다 승기프로님)
"""
N = int(input())

delta = ((1,1),(-1,1),(-2,0),(-1,-1),(1,-1),(2,0))
v = set()
v.add((0,0)) #출발지도 포함해줘야 출발지 == 도착지인지 알 수 있음
result = 0

def dfs(cnt,y,x,d):
    global result

    ny = y + delta[d][0]
    nx = x + delta[d][1]

    if (ny,nx) in v:
        if cnt == N:
            result += 1
        return

    if cnt == N:
        return

    new_dy = (d+1)%6
    new_dx = (d+5)%6 #-1 해도 똑같음

    v.add((ny,nx))

    dfs(cnt+1,ny,nx,new_dy)
    dfs(cnt+1,ny,nx,new_dx)

    v.remove((ny,nx)) #원복

if N <= 4:
    print(0)
else:
    dfs(0,0,0,0)
    print(result)
