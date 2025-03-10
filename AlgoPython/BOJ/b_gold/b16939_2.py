'''
위
앞
오
시계, 반시계
'''


def right(origin_cube):
    # 오른쪽 시계
    # 윗면에 앞면이옴
    cube_copy = [[_[:] for _ in __] for __ in origin_cube]
    cube_copy[0][0][1] = origin_cube[1][0][1]
    cube_copy[0][1][1] = origin_cube[1][1][1]
    # 앞면에 아랫면이옴
    cube_copy[1][0][1] = origin_cube[2][0][1]
    cube_copy[1][1][1] = origin_cube[2][1][1]
    # 아랫면에 뒷면이옴
    cube_copy[2][0][1] = origin_cube[5][1][0]
    cube_copy[2][1][1] = origin_cube[5][0][0]
    # 뒷면에 윗면이옴
    cube_copy[5][1][0] = origin_cube[0][0][1]
    cube_copy[5][0][0] = origin_cube[0][1][1]
    return cube_copy


def up(origin_cube):
    # 위
    # 앞면에 왼쪽
    cube_copy = [[_[:] for _ in __] for __ in origin_cube]
    cube_copy[1][0][0] = origin_cube[3][0][0]
    cube_copy[1][0][1] = origin_cube[3][0][1]
    # 왼쪽에 뒷면
    cube_copy[3][0][0] = origin_cube[5][0][0]
    cube_copy[3][0][1] = origin_cube[5][0][1]
    # 뒷면에 오른쪽면
    cube_copy[5][0][0] = origin_cube[4][0][0]
    cube_copy[5][0][1] = origin_cube[4][0][1]
    # 오른쪽면에 앞면
    cube_copy[4][0][0] = origin_cube[1][0][0]
    cube_copy[4][0][1] = origin_cube[1][0][1]
    return cube_copy


def front(origin_cube):
    # 앞 시계
    # 윗면에 왼쪽
    cube_copy = [[_[:] for _ in __] for __ in origin_cube]
    cube_copy[0][1][0] = origin_cube[3][1][1]
    cube_copy[0][1][1] = origin_cube[3][0][1]
    # 왼쪽에 아랫면
    cube_copy[3][1][1] = origin_cube[2][0][0]
    cube_copy[3][0][1] = origin_cube[2][0][1]
    # 아랫면 오른쪽면
    cube_copy[2][0][0] = origin_cube[4][1][0]
    cube_copy[2][0][1] = origin_cube[4][0][0]
    # 오른쪽면에 윗면
    cube_copy[4][1][0] = origin_cube[0][1][0]
    cube_copy[4][0][0] = origin_cube[0][1][1]
    return cube_copy


def rotation():
    global isOk, cube

    cube1 = right(cube)
    if same(cube1):
        isOk = True
        return
    cube2 = right(cube1)
    cube3 = right(cube2)

    if same(cube3):
        isOk = True
        return

    cube1 = up(cube)
    if same(cube1):
        isOk = True
        return
    cube2 = up(cube1)
    cube3 = up(cube2)

    if same(cube3):
        isOk = True
        return

    cube1 = front(cube)
    if same(cube1):
        isOk = True
        return
    cube2 = front(cube1)
    cube3 = front(cube2)

    if same(cube3):
        isOk = True
        return


def same(cube_):
    for face in cube_:
        first = face[0][0]
        for i in range(2):
            for j in range(2):
                if face[i][j] != first:
                    return False
    return True


colors = list(map(int, input().split()))
cube = [[[0] * 2 for j in range(2)] for i in range(6)]  # 4개씩 6개면
idx = 0
while colors:
    cube[idx][0][0] = colors.pop(0)
    cube[idx][0][1] = colors.pop(0)
    cube[idx][1][0] = colors.pop(0)
    cube[idx][1][1] = colors.pop(0)
    idx += 1

isOk = False
rotation()
if isOk:
    print(1)
else:
    print(0)
