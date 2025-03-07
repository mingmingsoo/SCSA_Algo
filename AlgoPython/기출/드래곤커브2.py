'''
문제설명
    드래곤 정보에 따라 끝점을 기준으로 시계 90도 회전
    격자 밖 걱정 안해도됨

구상
    이게 각 드래곤마다 그려주고 표시해야되는데...
    이게 어렵다.
    아 넘버링으로 하겠다. -> 아님.
입력
    드래곤 정보
주의 0과 101 시험해봐야함
'''

size =  101 #
grid = [[0] * size for i in range(size)]
dragon_num = int(input())  # 드래곤 총 몇개인지

col = [0, -1, 0, 1]
row = [1, 0, -1, 0]

for d_n in range(dragon_num):

    r, c, d, g = map(int, input().split())
    direction = [d]
    for i in range(g):
        N = len(direction)
        for j in range(N - 1, -1, -1):
            direction.append((direction[j] + 1) % 4)
    dragons = [(r, c)]
    for dd in direction:
        dragons.append((dragons[-1][0] + row[dd], dragons[-1][1] + col[dd]))
    for r, c in dragons:
        grid[r][c] = 1

ans = 0
for i in range(size - 1):
    for j in range(size - 1):
        if grid[i][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j + 1] == 1:
            ans += 1
print(ans)
