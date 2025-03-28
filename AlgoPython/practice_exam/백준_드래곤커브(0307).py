'''
백준 15685 드래곤커브
체감난이도 규칙 찾으면 골5
        규칙 못찾고 나처럼 풀었으면 골1..

정말정말 아쉬웠던 문제.
이 문제 이후로 아이디어나 코드 구상 안되면 규칙 찾을때까지 시간쓰기라고 다짐했습니다...
처음 풀었던 풀이는 다시 풀래도 못풀겠음.
'''
###################### 첫풀이(03.11)
# 머리 꼬리 남겨서 진짜 회전.
# 다시 풀라면 이렇게는 못풀 것 같습니다.

size = 202  # 101
grid = [[0] * size for i in range(size)]
dragon_num = int(input())  # 드래곤 총 몇개인지

row = [0, -1, 0, 1]
col = [1, 0, -1, 0]

for d_n in range(dragon_num):

    c, r, d, last_level = map(int, input().split())

    if last_level == 0:
        grid[r][c] = 1
        # 일단 0세대 만들어주기
        nr = r + row[d]
        nc = c + col[d]

        grid[nr][nc] = 1
        continue
    # 시작점
    ele_grid = [[0] * size for i in range(size)]

    ele_grid[r][c] = 2 # 머리표시
    # 일단 0세대 만들어주기
    nr = r + row[d]
    nc = c + col[d]
    ele_grid[nr][nc] = 1
    level = 1
    while level <= last_level:
        # print(nr, nc)
        # 끝점을 기준으로 시계 90도 회전
        # 맵은 level+1
        # print("===============")
        # for _ in ele_grid:
        #     print(_)

        new_size = 101
        small_grid = [[0] * new_size for i in range(new_size)]
        for i in range(new_size):
            for j in range(new_size):
                small_grid[i][j] = ele_grid[i + nr - (new_size) // 2][j + nc - (new_size) // 2]


        for i in range(size):
            for j in range(size):
                if ele_grid[i][j] ==2:
                    ele_grid[i][j] = 1
        #
        # print("===============")
        # for _ in small_grid:
        #     print(_)

        new_small_grid = [[0] * (new_size) for i in range(new_size)]
        for i in range(new_size):
            for j in range(new_size):
                new_small_grid[i][j] = small_grid[new_size - j - 1][i]

        # print("===============")
        # for _ in new_small_grid:
        #     print(_)
        for i in range(new_size):
            for j in range(new_size):
                if new_small_grid[i][j] != 0:
                    ele_grid[i + nr - (new_size) // 2][j + nc - (new_size) // 2] = new_small_grid[i][j]

        level += 1

        for i in range(size):
            for j in range(size):
                if ele_grid[i][j] ==2:
                    ele_grid[i][j] = 1
                    nr = i
                    nc = j
                    break
        ele_grid[r][c] = 2
        # for _ in ele_grid:
        #     print(*_)

    for i in range(size):
        for j in range(size):
            if ele_grid[i][j] != 0:
                grid[i][j] = 1

ans = 0
for i in range(size - 1):
    for j in range(size - 1):
        if grid[i][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j + 1] == 1:
            ans += 1
# for _ in grid:
#     print(*_)
print(ans)


##################### 두번째 풀이(03.11)
# 규칙
# 첫 방향에서 시작해서 그다음 방향은 뒤에서부터 반시계 회전해준 것임
# -> 방향 순서를 미리 담아놔야함.

n = int(input())
size = 101
grid = [[0] * size for i in range(size)]  # 답을 구하기 위해 만든 grid
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]
for dragon in range(n):
    r, c, first_d, gener = map(int, input().split())
    # 방향 배열 만들기
    dirs = [first_d]
    for g in range(gener):
        for i in range(len(dirs) - 1, -1, -1):
            dirs.append((dirs[i] + 1) % 4)  # 끝점을 기준으로 반시계회전한 방향을 넣어준다.
    lotation = [(r, c)]
    for d in dirs:
        nr, nc = lotation[-1]  # 끝점을 기준으로 연산해서 넣어준다!
        lotation.append((nr + row[d], nc + col[d]))
    for r, c in lotation:
        grid[r][c] = 1
ans = 0
for i in range(size - 1):
    for j in range(size - 1):
        if grid[i][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j] == 1 and grid[i + 1][j + 1] == 1:
            ans += 1
print(ans)
