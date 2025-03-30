T = int(input())
for tc in range(T):
    '''
    서현이 코드 참조
    '''

    face_dict = {
        "U": [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
        "D": [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
        "F": [[18, 19, 20], [21, 22, 23], [24, 25, 26]],
        "B": [[27, 28, 29], [30, 31, 32], [33, 34, 35]],
        "L": [[36, 37, 38], [39, 40, 41], [42, 43, 44]],
        "R": [[45, 46, 47], [48, 49, 50], [51, 52, 53]]
    }

    side_dict = {
        "U": [20, 19, 18, 38, 37, 36, 29, 28, 27, 47, 46, 45],
        "D": [24, 25, 26, 51, 52, 53, 33, 34, 35, 42, 43, 44],
        "F": [6, 7, 8, 45, 48, 51, 11, 10, 9, 44, 41, 38],
        "B": [2, 1, 0, 36, 39, 42, 15, 16, 17, 53, 50, 47],
        "L": [0, 3, 6, 18, 21, 24, 9, 12, 15, 35, 32, 29],
        "R": [8, 5, 2, 27, 30, 33, 17, 14, 11, 26, 23, 20]
    }

    order_num = int(input())
    order_list = list(input().split())
    dice = ["w"] * 9 + ["y"] * 9 + ["r"] * 9 + ["o"] * 9 + ["g"] * 9 + ["b"] * 9
    for order in order_list:
        f, d = order[0], order[1]

        face = face_dict[f]
        face_copy = [_[:] for _ in face]
        if d == "+":
            for i in range(3):
                for j in range(3):
                    face[i][j] = face_copy[j][3 - i - 1]
        else:
            for i in range(3):
                for j in range(3):
                    face[i][j] = face_copy[3 - j - 1][i]
        side_copy = side_dict[f]
        if d == "+":
            side = side_copy[-3:] + side_copy[:-3]
        else:
            side = side_copy[3:] + side_copy[:3]

        dice_copy = dice[:]
        for r in range(3):
            for c in range(3):
                dice[face[r][c]] = dice_copy[face_copy[r][c]]

        for w in range(12):
            dice[side_copy[w]] = dice_copy[side[w]]

    num = 0
    for i in range(3):
        for j in range(3):
            print(dice[num], end="")
            num += 1
        print()
