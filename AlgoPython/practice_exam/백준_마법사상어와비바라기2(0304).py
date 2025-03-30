'''
# 백준 21610 마법사 상어와 비바라기 (코드트리 나무 타이쿤)
# 세번째 풀이
    1차원으로 풀어보기
    이상하네 시간이 더 기네... append 때문인 것 같음.
    -> set으로 관리하고 is_bug 없애도 무방함. -> 겹칠 수가 없음
'''
n, move_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

move_list = [list(map(int, input().split())) for i in range(move_num)]

row = [0, -1, -1, -1, 0, 1, 1, 1]
col = [-1, -1, 0, 1, 1, 1, 0, -1]

row2 = [1, 1, -1, -1]
col2 = [1, -1, 1, -1]

# 초기 구름 설정
is_cloud = set([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for d, s in move_list:
    d -= 1

    # 모든 구름이 di 방향으로 si칸 이동한다.
    is_new_cloud = set()
    for r, c in is_cloud:
        nr = (r + row[d] * s) % n
        nc = (c + col[d] * s) % n
        is_new_cloud.add((nr,nc))
        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        grid[nr][nc] += 1

    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다
    for r, c in is_new_cloud:
        round_water = 0
        for k in range(4):
            nr = r + row2[k]
            nc = c + col2[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if grid[nr][nc] > 0:
                grid[r][c] +=1

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    is_cloud = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and (i, j) not in is_new_cloud:
                is_cloud.add((i, j))
                grid[i][j] -= 2

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]

print(ans)
