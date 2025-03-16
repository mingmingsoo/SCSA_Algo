'''
땡스 투 완진
return 안써보기
'''
n = int(input())
grid = [[0] * 100 for i in range(100)]
#  위 아래  ↖  ↘   ↗  ↙
row = [-1, 1, -1, 1, -1, 1]
col = [0, 0, -2, 2, 2, -2]
grid[50][50] = 1
grid[49][50] = 1
ans = 0
dirs_info = {0: (2, 4), 1: (3, 5), 2: (0, 5), 3: (1, 4), 4: (0, 3), 5: (2, 1)}


def dfs(r, c, cnt, dirs):
    global ans
    if cnt != n:
        for k in dirs_info[dirs]:
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < 100 and 0 <= nc < 100):
                continue
            if cnt == n - 1 and grid[nr][nc] == 1:
                ans += 1
            if grid[nr][nc] == 0:
                grid[nr][nc] = 1
                dfs(nr, nc, cnt + 1, k)
                grid[nr][nc] = 0


dfs(49, 50, 0, 0)  # 처음엔 위로
print(ans)


#
# n = int(input())
# grid = [[0] * 100 for i in range(100)]
# #  위 아래  ↖  ↘   ↗  ↙
# row = [-1, 1, -1, 1, -1, 1]
# col = [0, 0, -2, 2, 2, -2]
# grid[50][50] = 1
# grid[49][50] = 1
# ans = 0
# dirs_info = {0: (2, 4), 1: (3, 5), 2: (0, 5), 3: (1, 4), 4: (0, 3), 5: (2, 1)}
#
#
# def dfs(r, c, cnt, dirs):
#     global ans
#     if cnt == n:
#         return
#     for k in dirs_info[dirs]:
#         nr = r + row[k]
#         nc = c + col[k]
#         if not (0 <= nr < 100 and 0 <= nc < 100):
#             continue
#         if cnt == n - 1 and grid[nr][nc] == 1:
#             ans += 1
#         if grid[nr][nc] == 0:
#             grid[nr][nc] = 1
#             dfs(nr, nc, cnt + 1, k)
#             grid[nr][nc] = 0
#
#
# dfs(49, 50, 0, 0)  # 처음엔 위로
# print(ans)
