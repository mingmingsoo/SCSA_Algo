'''
덱 2차원 배열 만들기
시간 차이는 없음 몸이 편함
'''
from collections import deque

n, m, order_num = map(int, input().split())
grid = [deque(map(int, input().split())) for i in range(n)]
for o in range(order_num):
    x, d, k = map(int, input().split())
    if d == 0: d = 1
    else: d = -1
    k = k % m
    # 회전
    for i in range(x - 1, n, x):  # x 의 배수인 애들 회전
        grid[i].rotate(d*k)

    is_delete = False
    delete = [[0] * m for i in range(n)]
    # 1. 같은 원 확인
    for i in range(n):
        for j in range(-1, m - 1):  # 0하고 m-1은 연결된다.
            if grid[i][j] != 0:
                if grid[i][j] == grid[i][j + 1]:
                    delete[i][j], delete[i][j + 1] = 1, 1
                    is_delete = True

    # 2. 세로 확인
    for j in range(m):
        for i in range(n - 1):
            if grid[i][j] != 0:
                if grid[i][j] == grid[i + 1][j]:
                    delete[i][j], delete[i + 1][j] = 1, 1
                    is_delete = True

    # 삭제가능하면 삭제
    if is_delete:
        for i in range(n):
            for j in range(m):
                if delete[i][j] == 1:
                    grid[i][j] = 0
    # 아니라면 평균 구하기
    else:
        cnt = sm = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    cnt += 1
                    sm += grid[i][j]

        for i in range(n):
            for j in range(m):
                if grid[i][j] <= 0:
                    continue
                if grid[i][j] < (sm / cnt): grid[i][j] += 1
                elif grid[i][j] > (sm / cnt): grid[i][j] -= 1

ans = sum(map(sum, grid))
print(ans)
