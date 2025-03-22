'''
문제 설명
    궁수 3명 배치
    맨 아래 행에
출력
    궁수 공격으로 죽인 적
'''

n, m, limit = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)] + [[0] * m]  # 패딩

sel = [0] * 3  # 선택할 열
ans = 0


def combi(sidx, idx):
    global ans
    if sidx == 3:
        game_grid = [_[:] for _ in grid]
        # 여기서 게임 시작
        kill = 0
        while True:
            # 궁수 공격
            kill_lst = []
            for jdx in sel:
                ele_kill_lst = []
                for i in range(n):
                    for j in range(m):
                        if game_grid[i][j]:
                            dist = abs(n - i) + abs(jdx - j)
                            if dist <= limit:
                                ele_kill_lst.append((dist, (j, i)))
                if ele_kill_lst:
                    ele_kill_lst.sort()
                    d, lo = ele_kill_lst[0]
                    kill_lst.append(lo)

            for c, r in kill_lst:
                if game_grid[r][c] == 1:
                    game_grid[r][c] = 0
                    kill += 1

            # 적 내려와
            game_grid.pop()
            game_grid.insert(0, [0] * m)

            # 적 없는지 검사
            enemy = 0
            for i in range(n):
                for j in range(m):
                    if game_grid[i][j]: enemy += 1
            if not enemy:
                break
        ans = max(ans, kill)

        return
    if idx == m:
        return
    sel[sidx] = idx
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
print(ans)
