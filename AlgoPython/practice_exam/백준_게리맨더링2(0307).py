'''
# 코드트리 종전
2025.03.30.일
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 19:08
    1차 제출  19:55
    문제 종료 20:01

    총 풀이시간 53분
        08~13 : 문제 이해(5)
                백준과 달리 대각선 범위가 없어서 당황...
                -> 손으로 계산하기
        13~20 : 윗점, 대각선 2개 길이 범위 잡기(7)
                 -> 잘 잡혔나 확인
        20~55 : 영역 나누기(35)
                print 찍어서 잘 나눠졌는지 확인.....
        55~01 : 틀린 테케 디버깅(6)
                아까 했던 print 다시 찍어서
                어느 영역이 잘못됐는지 확인
                3,4 영역 재계산 해서 수정!!!!


  메모리 24 MB
  시간 438 ms

  회고
    1. 백준에는 대각선 범위와 1,2,3,4 범위가 주어졌는데
        코드트리는 그렇지 않아서 2배는 어렵게 느껴졌음...
        결국 이 범위로 1회 틀 ㅠㅠㅠ
        범위 없으니까 그냥 첨보는 문제 같았달까........


# 문제 풀면서의 기록
대각선이 될 수 있는 범위는 1~n-1
대각선의 길이도 1~n-1

헉 대각선 범위도 셀프임 ;;;
'''
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
row = [1, 1]
col = [-1, 1]

ans = int(1e9)


def cal(i, j, d1, d2):
    global ans
    area = [[0] * n for i in range(n)]
    r, c = i, j
    for d in range(d1):
        area[r][c] = 5
        nr = r + row[0]
        nc = c + col[0]
        r = nr
        c = nc
    for d in range(d2 + 1):
        area[r][c] = 5
        nr = r + row[1]
        nc = c + col[1]
        r = nr
        c = nc

    r, c = i, j
    for d in range(d2):
        area[r][c] = 5
        nr = r + row[1]
        nc = c + col[1]
        r = nr
        c = nc

    for d in range(d1):
        area[r][c] = 5
        nr = r + row[0]
        nc = c + col[0]
        r = nr
        c = nc

    for r in range(i + d1):
        for c in range(j + 1):
            if area[r][c] != 5:
                area[r][c] = 1
            else:
                break

    for r in range(i + d2 + 1):
        for c in range(n - 1, j, -1):
            if area[r][c] != 5:
                area[r][c] = 2
            else:
                break

    for r in range(i + d1, n):
        for c in range(j - d1 + d2):
            if area[r][c] != 5:
                area[r][c] = 3
            else:
                break

    for r in range(i + d2 + 1, n):
        for c in range(n - 1, j+d2-d1-1, -1):
            if area[r][c] != 5:
                area[r][c] = 4
            else:
                break

    one, two, three, four, five = 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if area[i][j] == 1:
                one += grid[i][j]
            elif area[i][j] == 2:
                two += grid[i][j]
            elif area[i][j] == 3:
                three += grid[i][j]
            elif area[i][j] == 4:
                four += grid[i][j]
            else:
                five += grid[i][j]

    tmp = [one, two, three, four, five]
    ans = min(max(tmp) - min(tmp), ans)


for i in range(n - 1):
    for j in range(n - 1):
        # 얘가 윗점이 될 거임
        for d1 in range(1, n - 1):
            for d2 in range(1, n - 1):
                # 대각선 길이
                if j - d1 >= 0 and j + d2 < n and i + d1 + d2 < n:
                    cal(i, j, d1, d2)
print(ans)


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
