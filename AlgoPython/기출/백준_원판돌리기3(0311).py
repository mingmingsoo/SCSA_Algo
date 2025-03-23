'''
슬라이싱 사용
서현프로 코드참조

아 이래서 제로디비젼이 나는구나!~!!!~!~~! 오키오키 확인
'''

n, m, order_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
for o in range(order_num):
    x, d, k = map(int, input().split())
    k = k % m
    # 회전
    for i in range(x - 1, n, x):  # x 의 배수인 애들 회전
        if d == 1:
            grid[i] = grid[i][k:] + grid[i][:k]
        elif d == 0:
            grid[i] = grid[i][-k:] + grid[i][:-k]
    # 회전 끝

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
        if cnt != 0:
            avg = sm / cnt
            for i in range(n):
                for j in range(m):
                    if grid[i][j] <= 0:
                        continue
                    if grid[i][j] < avg:
                        grid[i][j] += 1
                    elif grid[i][j] > avg:
                        grid[i][j] -= 1
        else:
            break

ans = sum(map(sum, grid))
print(ans)
