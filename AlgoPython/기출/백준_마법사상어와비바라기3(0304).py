'''
# 다섯번째 풀이

    2차원 배열에서 isbug 없애기

'''
n, move_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

move_list = [list(map(int, input().split())) for i in range(move_num)]

row = [0, -1, -1, -1, 0, 1, 1, 1]
col = [-1, -1, 0, 1, 1, 1, 0, -1]

row2 = [1, 1, -1, -1]
col2 = [1, -1, 1, -1]

# 초기 구름 설정
is_cloud = [[False] * n for i in range(n)]
is_cloud[n - 1][0], is_cloud[n - 1][1], is_cloud[n - 2][0], is_cloud[n - 2][1] = True, True, True, True

for d, s in move_list:
    d -= 1

    # 모든 구름이 di 방향으로 si칸 이동한다.
    is_new_cloud = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if is_cloud[i][j]:
                nr = (i + row[d] * s) % n
                nc = (j + col[d] * s) % n
                is_new_cloud[nr][nc] = True

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for i in range(n):
        for j in range(n):
            if is_new_cloud[i][j]:
                grid[i][j] += 1

    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다

    for i in range(n):
        for j in range(n):
            if is_new_cloud[i][j]:
                for k in range(4):
                    nr = i + row2[k]
                    nc = j + col2[k]
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if grid[nr][nc] > 0:
                        grid[i][j] += 1

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    is_cloud = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and not is_new_cloud[i][j]:
                is_cloud[i][j] = True
                grid[i][j] -= 2

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]

print(ans)
