'''
두번째 풀이: 방향전환 간단하게

문제설명
    / \ 만나면 방향이 90도 바뀐다
    시그널이 블랙홀 또는 범위에 벗어날 떄까지 돈다
    이 도는 걸 최대로 돌게끔 해야함

입력
    C가 블랙홀
    시작 위치
출력
    가장 긴 시간. 방향 앞에꺼먼저
    사이클이면 보이저!
구상
    시작점에서 4방향 탐색
    사이클? 은 첫점으로 같은 방향으로 돌아왔음을 의미

'''
def do(r, c, d):
    global is_cycle
    sr, sc, sd = r, c, d  # 처음 위치
    t = 1
    while True:

        nr = r + row[d]
        nc = c + col[d]

        if not (0 <= nr < n and 0 <= nc < m):
            return t

        if nr == sr and nc == sc and d == sd:
            is_cycle = True
            return 0

        if grid[nr][nc] == "/":
            if d == 0 or d == 1:
                d = 1 - d
            else:
                d = 5 - d

        elif grid[nr][nc] == "\\":
            d = 3 - d

        elif grid[nr][nc] == "C":
            return t
        t += 1
        r = nr
        c = nc


n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
sr, sc = map(lambda x: int(x) - 1, input().split())
dir = "U"
time = 0
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
is_cycle = False


for k in range(4):
    ele_time = do(sr, sc, k)
    if (ele_time > time):
        time = ele_time
        dir = "URDL"[k]
    if (is_cycle):
        dir = "URDL"[k]
        break

if is_cycle:
    print(dir)
    print("Voyager")
else:
    print(dir)
    print(time)
