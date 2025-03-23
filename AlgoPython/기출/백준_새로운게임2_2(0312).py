'''
# 17837 백준 새로운 게임2
두번째 풀이 원래 계획했던 대로 풀어보기.
'''

n, horse_num = map(int, input().split())
color = [list(map(int, input().split())) for i in range(n)]
grid = [[[] for i in range(n)] for i in range(n)]  # 말 넘버만 담아줌.
horse_list = []
for horse in range(horse_num):
    r, c, d = map(int, input().split())
    grid[r - 1][c - 1].append(horse)  # 넘버링, 방향
    horse_list.append([r - 1, c - 1, d - 1])

ans = -1

row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
move = {0: 1, 1: 0, 2: 3, 3: 2}


def valid():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) >= 4:
                return True
    return False


def is_range(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


for turn in range(1, 1001):
    find = False
    for i in range(horse_num):
        r, c, d = horse_list[i]
        if not is_range(r + row[d], c + col[d]) or color[r + row[d]][c + col[d]] == 2:
            # 방향 전환 필요
            horse_list[i][2] = move[d]
        # 이동할 위치
        r, c, d = horse_list[i]
        nr = r + row[d]
        nc = c + col[d]
        if not is_range(nr, nc) or color[nr][nc] == 2:
            continue
        for j in range(len(grid[r][c])):
            if grid[r][c][j] == i:
                move_list = grid[r][c][j:]
                if color[nr][nc] == 1:
                    move_list = move_list[::-1]

                grid[nr][nc].extend(move_list)
                grid[r][c] = grid[r][c][:j]
                for num in move_list:
                    horse_list[num][0] = nr
                    horse_list[num][1] = nc
                break
        if valid():
            ans = turn
            find = True
            break
    if find:
        break

print(ans)
