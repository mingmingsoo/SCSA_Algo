'''

# 백준 17140 이차원 배열과 연산 (코드트리 격자 숫자 놀이)
# 두번째 풀이
    함수화, 전치행렬 간단히
'''


def my_sort(r_size, c_size, category):
    max_row_size = 0
    for i in range(r_size):
        count = [0] * 101 # 몇개있는지 세줄거임
        for j in range(c_size):
            if category == "R":
                if grid[i][j] == 0:
                    continue
                count[grid[i][j]] += 1
            elif category == "C":
                if grid[j][i] == 0: # 0인애들 빼고
                    continue
                count[grid[j][i]] += 1 # 갯수 세거라.
        sort_list = []
        for i in range(101):
            if count[i] > 0: # 정렬!
                sort_list.append((i, count[i]))
        sort_list.sort(key=lambda x: (x[1], x[0]))  # 정렬 !
        max_row_size = max(len(sort_list) * 2, max_row_size)
        tmp = []
        for idx, cnt in sort_list:
            tmp.extend([idx, cnt])
        new_grid.append(tmp)
    # 2. 최대 크기 기준으로 맞춰주기
    for row in new_grid:
        if len(row) < max_row_size:
            row += [0] * (max_row_size - len(row))


er, ec, target = map(int, input().split())
er -= 1
ec -= 1
ans = -1
grid = [list(map(int, input().split())) for i in range(3)]

for time in range(101):

    # 0. 목표 달성 검사
    if 0 <= er < len(grid) and 0 <= ec < len(grid[0]) and grid[er][ec] == target:
        ans = time
        break

    # 1. 크기에 따른 R,C 연산
    r_size, c_size = len(grid), len(grid[0])
    new_grid = []
    if r_size >= c_size:
        my_sort(r_size, c_size, "R")
    else:
        my_sort(c_size, r_size, "C")
        new_grid = list(zip(*new_grid))  # 전치 필요

    # 3. 행 or 열 크기가 100 넘어가면 버려주기.
    r_size, c_size = len(new_grid), len(new_grid[0])
    is_small_need = False
    if r_size > 100:
        is_small_need = True
        r_size = 100
    if c_size > 100:
        is_small_need = True
        c_size = 100

    if is_small_need:
        grid = [_[:100] for _ in new_grid[:100]]
    else:
        grid = new_grid

print(ans)
