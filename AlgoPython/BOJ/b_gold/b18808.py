n, m, sticker_num = map(int, input().split())
grid = [[0] * m for i in range(n)]

def rotation():
    global sticker,sn,sm
    # sticker를 회전시킴
    ro_sticker = [[0]* sn for i in range(sm)]

    for i in range(sm):
        for j in range(sn):
            ro_sticker[i][j] = sticker[sn-j-1][i]

    sticker = ro_sticker
    sn, sm = sm, sn

def isOk(r, c):
    for i in range(sn):
        for j in range(sm):
            if sticker[i][j] == 1 and grid[i + r][j + c] == 1:
                return False
    return True


def isfill(r,c):
    for i in range(sn):
        for j in range(sm):
            if sticker[i][j] == 1:
                grid[i+r][j+c] = 1


for sti in range(sticker_num):
    sn, sm = map(int, input().split())
    sticker = [list(map(int, input().split())) for i in range(sn)]

    glue = False
    for ro in range(4): # 4임
        for i in range(n - sn + 1):  # 5 - 3 = 2
            for j in range(m - sm + 1):
                if isOk(i, j):
                    glue = True
                    isfill(i, j)
                    break
            if glue:
                break
        if glue:
            break
        else:
            rotation()

    # 0,0에서 n,m 까지 붙일 수 있는 곳 찾기
    # 없었으면 회전하기
    # 다시 0,0에서 n,m 까지 붙일 수 있는 곳 찾기
    # print("-----------")
    # for _ in grid:
    #     print(*_)

ans = 0
print(sum(map(sum, grid)))