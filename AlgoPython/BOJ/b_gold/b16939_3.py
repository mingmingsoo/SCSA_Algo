'''
노 하드코딩
나연이 코드 영감받아서...
'''
from collections import deque

cube = list(map(int, input().split()))
# left = [1, 3, 5, 7, 9, 11, 24, 22]
# up = [13, 14, 5, 6, 17, 18, 21, 22]
# front = [3, 4, 17, 19, 10, 9, 16, 14]

face = [[0, 2, 4, 6, 8, 10, 23, 21], [12, 13, 4, 5, 16, 17, 20, 21], [2, 3, 16, 18, 9, 8, 15, 13]]


def roro():
    for i in range(3):
        for rotation in (-2, 2):
            possible = True
            ro_cube = cube[:]
            for k in range(8):
                ro_cube[face[i][k]] = cube[face[i][(k + rotation) % 8]]
            for f in range(0, 24, 4):
                if len(set(ro_cube[f:f + 4])) != 1:
                    possible = False
                    break
            if possible:
                return True

    return False


if roro():
    print(1)
else:
    print(0)
