'''
20:55~21:20
예상풀이시간:40분
실제 풀이시간:25분

문제 설명
    뭐 ,, 돌을 놓을 수 있는 곳에만 위치를 준다고 하고
    그 상대편 돌들을 바꾸는 게 관건임
헷갈렸던 점
    문제를 끝까지 다 안읽고 조건을 생각해서
    내가 두려웠던 건 돌을 놓을 수 있는 조건? 같은 거였는데
    입력에서 알아서 놓을 수 있는데만 준다고 한거보고 안심했음
    문제를 전체적으로 한번읽고 분석하는 습관 가지기

입력
    1 흑
    2 백
'''

row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]
def change(r, c, color):
    sr, sc = r, c # 초기 위치 남겨주기 -> r = nr로 갱신할거라서
    for k in range(8):
        r = sr
        c = sc
        mycolor = False
        change_color = set() # 조건에 해당하면 한번에 바꿔줄거임
        while True:
            nr = r + row[k]
            nc = c + col[k]

            if not (0 <= nr < n and 0 <= nc < n):
                break
            if grid[nr][nc] == color: # 나와 같은 색을 발견하면 그 사이 애들은 바꿀 수 있는 것
                mycolor = True
                break # 그리고 더 탐색하면 안돼서 종료
            elif grid[nr][nc] != 0: # 나와 다른색이고 0이 아니면
                change_color.add((nr, nc)) # 바꿀 수 있으니 담아주기
                r = nr # 위치 갱신
                c = nc
            else:
                break # 0이면 즉 빈칸이면 종료

        # 색깔 한번에 바꿔주기
        if mycolor:
            for i, j in change_color:
                grid[i][j] = color

T = int(input())
for tc in range(T):

    n, m = map(int, input().split())
    grid = [[0] * n for i in range(n)]

    # 초기 위치 세팅
    grid[n // 2 - 1][n // 2 - 1] = 2
    grid[n // 2 - 1][n // 2] = 1
    grid[n // 2][n // 2 - 1] = 1
    grid[n // 2][n // 2] = 2

    for i in range(m):
        r, c, color = map(int, input().split())
        r -= 1
        c -= 1
        grid[r][c] = color
        change(r, c, color)

    # 출력
    b = 0
    w = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                b += 1
            elif grid[i][j] == 2:
                w += 1

    print(f"#{tc+1} {b} {w}")