'''
구상
    AB, AC, ..., EF의 경기 -> 총 15가지의 경기에서 승,무,패 3가지 경우의 수를 모두 따져줘야함.
    중복순열로 행렬을 채우고, 오리지널과 비교한다.
    완탐이라 3**15 = 14348907 이긴한데 가지치기해서... 매직스타처럼 가능한 경우만 가게끔 했습니다.
'''

def isok(grid):
    global find
    sel = [0] * 15  # 1,2,3 선택할 수 있음
    find = False
    perm(0, grid, sel)
    if find:
        return True
    else:
        return False

def perm(idx, grid, sel):
    global find
    if find:
        return
    if not isvalid(idx, sel, grid):
        return
    if idx == 15:
        find = True
        return

    for i in range(1, 4):
        sel[idx] = i
        perm(idx + 1, grid, sel) # 중복순열

def isvalid(idx, sel, grid):
    score_grid = [[0] * 6 for i in range(6)]
    ii = 0
    for i in range(6):
        for j in range(6):
            if ii >= idx and idx < 15: # idx < 15 이게 없으면 마지막 F 검사를 안함
                return True
            if i == j or i > j:
                continue
            score_grid[i][j] = sel[ii]
            score_grid[j][i] = 4 - sel[ii]
            ii += 1

        win = score_grid[i].count(1)
        moo = score_grid[i].count(2)
        lose = score_grid[i].count(3)
        if (win != grid[i][0] or moo != grid[i][1] or lose != grid[i][2]):
            return False
    return True



# 초기 입력 세팅
game = []

for i in range(4):
    tmp_arr = list(map(int, input().split()))
    tmp_grid = [[0] * 3 for i in range(6)]
    idx = 0
    for i in range(6):
        for j in range(3):
            tmp_grid[i][j] = tmp_arr[idx]
            idx += 1
    game.append(tmp_grid)

# 출력 배열
ans = []

for grid in game:
    find = False # 하나라도 찾으면 튀어나올거임
    if (isok(grid)):
        ans.append(1)
    else:
        ans.append(0)
print(*ans)
