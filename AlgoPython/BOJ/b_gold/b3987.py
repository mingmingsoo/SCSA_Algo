'''
문제 설명
    시그널이 내부에서 가장 오래 돌 수 있는 시간은?
    시그널은 범위를 벗어나거나, 블랙홀을 만나면 사라진다.
입력
    N, M
    맵(/\ : 행성, C : 블랙홀, . : 빈칸)
    탐사선 위치 r,c
출력
    탐사선 위치에서 어떤 방향이 최대시간을 가지는지
    최대시간
    * 무한으로 돈다면 Voyager 출력
구상
    초기 위치에서 4가지 방향 완탐.
    초기 위치로 돌아온다면  Voyager 출력
틀린이유
    로직은 맞았는데
    재귀를 타면 안되는 문제였나봄
    while로 돌리니까 해결,,,, 하
'''

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
sr, sc = map(lambda x: int(x) - 1, input().split())

dir = ""
max_time = 0
cycle = False

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def tracking(r, c, d, time, sd):
    global dir, max_time, cycle

    while True:
        nr = r + row[d]
        nc = c + col[d]
        # 범위 벗어나면 끝
        if not (0 <= nr < n and 0 <= nc < m):
            if time > max_time:
                max_time = time
                dir = "URDL"[sd]
            return

        # 블랙홀 만나면 끝
        if grid[nr][nc] == "C":
            if time > max_time:
                max_time = time
                dir = "URDL"[sd]
            return

        # 시작 위치 만나면 사이클 끝
        if nr == sr and nc == sc and d == sd:
            cycle = True
            dir = "URDL"[sd]
            return

        # 행성 만나면 방향 전환
        if grid[nr][nc] == "/":
            if (d == 0):
                d = 1
            elif (d == 1):
                d = 0
            elif (d == 2):
                d = 3
            else:
                d = 2

        if grid[nr][nc] == "\\":
            if (d == 0):
                d = 3
            elif (d == 1):
                d = 2
            elif (d == 2):
                d = 1
            else:
                d = 0
        r = nr
        c = nc
        time += 1


for i in range(4):
    tracking(sr, sc, i, 1, i)
    if (cycle):
        print(dir)
        print("Voyager")
        break
if (not cycle):
    print(dir)
    print(max_time)
