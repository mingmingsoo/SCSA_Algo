'''
# 백준 17779 게리맨더링2
# 체감난이도 골4 - 인데.. 드래곤커브로 멘탈 무너지고 푸니 대각선 처리하는 방법이 생각이 안나서 못풀었었습니다.
# 정규시간 이후에 마음 비우고 푸니 대략 40분정도 걸렸던 것 같습니다.ㅜㅜ
# 기록을 못한 것이 아쉽습니다.

문제 구상
1. 브루투푸스와 시뮬레이션
2. 1234는 사각형의 범위이므로 5먼저 채워주고
    1234를 채워주다가 5를 만나면 break하게 했다.

'''

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
ans = 100 * 20 * 20 + 1
row = [1, 1] # 5번 구역을 위한 방향좌표
col = [-1, 1]


def do(x, y, d1, d2):
    global ans
    location = [[0] * n for i in range(n)]
    # 대각선 부터 채우기
    # ↙ ↘
    r, c = x, y
    for d in range(d1 + 1):
        location[r][c] = 5
        r = r + row[0]
        c = c + col[0]
    r, c = r - row[0], c - col[0]
    for d in range(d2 + 1):
        location[r][c] = 5
        r = r + row[1]
        c = c + col[1]
    # ↘ ↙
    r, c = x, y
    for d in range(d2 + 1):
        location[r][c] = 5
        r = r + row[1]
        c = c + col[1]
    r, c = r - row[1], c - col[1]
    for d in range(d1 + 1):
        location[r][c] = 5
        r = r + row[0]
        c = c + col[0]

    # 1
    for i in range(x + d1):
        for j in range(y + 1):
            if location[i][j] == 5:
                break
            location[i][j] = 1
    # 2
    for i in range(x + d2 + 1):
        for j in range(n - 1, y, -1):
            if location[i][j] == 5:
                break
            location[i][j] = 2
    # 3
    for i in range(x + d1, n):
        for j in range(y - d1 + d2):
            if location[i][j] == 5:
                break
            location[i][j] = 3
    # 4
    for i in range(x + d2 + 1, n):
        for j in range(n - 1, y - d1 + d2 - 1, -1):
            if location[i][j] == 5:
                break
            location[i][j] = 4

    a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if location[i][j] == 0 or location[i][j] == 5:
                a5 += grid[i][j]
            elif location[i][j] == 1:
                a1 += grid[i][j]
            elif location[i][j] == 2:
                a2 += grid[i][j]
            elif location[i][j] == 3:
                a3 += grid[i][j]
            elif location[i][j] == 4:
                a4 += grid[i][j]

    ans = min(ans, max(a1, a2, a3, a4, a5) - min(a1, a2, a3, a4, a5))


for i in range(n):
    for j in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if (0 <= i < i + d1 + d2 <= n - 1 and 0 <= j - d1 < j < j + d2 <= n - 1):
                    do(i, j, d1, d2)
print(ans)
