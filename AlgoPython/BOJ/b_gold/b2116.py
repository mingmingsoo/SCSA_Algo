'''
문제설명
    주사위를 쌓을 수 있는 모든 경우의 수에서 옆면의 최댓값을 구해라
구상
    1. 맨 밑에 뭘 쌓을지 정한다
        - >어느면이 윗면이 될지는 경우의 수 6개
        -> 그러면 나머지는 맞춰가야하는거라 정해짐
'''
import sys

sys.setrecursionlimit(10 ** 5)
n = int(input())
dice = [list(map(int, input().split())) for i in range(n)]

maxi = 0


def go(top, bottom, face, idx):  # 위 아래 옆
    global maxi
    if (idx == n):
        maxi = max(maxi, face)
        return
    # 이제 두번째 주사위의 열을 맞춰줘야함.
    visited = [False] * 6
    cur_top, cur_bottom = -1, top
    cur_bottom_idx = -1
    for i in range(6):
        if dice[idx][i] == top:
            visited[i] = True
            cur_bottom_idx = i
            break

    if cur_bottom_idx == 0:
        cur_top = dice[idx][5]
        visited[5] = True
    elif cur_bottom_idx == 1:
        cur_top = dice[idx][3]
        visited[3] = True
    elif cur_bottom_idx == 2:
        cur_top = dice[idx][4]
        visited[4] = True
    elif cur_bottom_idx == 3:
        cur_top = dice[idx][1]
        visited[1] = True
    elif cur_bottom_idx == 4:
        cur_top = dice[idx][2]
        visited[2] = True
    elif cur_bottom_idx == 5:
        cur_top = dice[idx][0]
        visited[0] = True

    ele_maxi = 0
    for i in range(6):
        if not visited[i]:
            ele_maxi = max(ele_maxi, dice[idx][i])
    go(cur_top, cur_bottom, face + ele_maxi, idx + 1)


for i in range(6):
    visited = [False] * 6
    visited[i] = True
    first_top = dice[0][i]  # 윗면
    first_bottom = -1
    if i == 0:
        first_bottom = dice[0][5]
        visited[5] = True
    elif i == 1:
        first_bottom = dice[0][3]
        visited[3] = True
    elif i == 2:
        first_bottom = dice[0][4]
        visited[4] = True
    elif i == 3:
        first_bottom = dice[0][1]
        visited[1] = True
    elif i == 4:
        first_bottom = dice[0][2]
        visited[2] = True
    elif i == 5:
        first_bottom = dice[0][0]
        visited[0] = True

    ele_maxi = 0
    for i in range(6):
        if not visited[i]:
            ele_maxi = max(ele_maxi, dice[0][i])
    go(first_top, first_bottom, ele_maxi, 1)
print(maxi)
