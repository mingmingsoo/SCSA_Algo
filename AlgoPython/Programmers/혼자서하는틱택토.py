'''
문제 설명
    이 게임이 정상적으로 진행 되었는가?
구상
    정상적이지 않은 경우:
    O==X인데 Oline이 더 많거나 같은 경우
    O>X인데 Xline이 더 많거나 같은 경우
'''


def isKaro(r, c, char, board):
    for j in range(1, 3):
        if board[r][j] != char:
            return False
    return True


def isSero(r, c, char, board):
    for i in range(1, 3):
        if board[i][c] != char:
            return False
    return True


def isX(r, c, char, board):
    for i in range(1, 3):
        for j in range(1, 3):
            if (i != j):
                continue
            if board[i][j] != char:
                return False
    return True


def isY(r, c, char, board):
    for i in range(1, -1, -1):
        for j in range(1, 3):
            if (i + j != 2): # 여기서 틀렸었음 ㅎ
                continue
            if board[i][j] != char: 
                return False
    return True


def game(board):
    O = 0
    X = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "O"):
                O += 1
            elif (board[i][j] == "X"):
                X += 1
    if O == X + 1 or O == X:
        pass
    else:
        return False
    xline = 0
    oline = 0
    for i in range(3):
        for j in range(3):
            if i != 0 and j != 0:
                continue
            if board[i][j] == ".":
                continue
            print(i, j)
            if i == 0:
                if (isSero(i, j, board[i][j], board)):
                    if (board[i][j] == "O"):
                        oline += 1
                    else:
                        xline += 1
            if j == 0:
                if (isKaro(i, j, board[i][j], board)):
                    if (board[i][j] == "O"):
                        oline += 1
                    else:
                        xline += 1
            if i == j == 0:
                if (isX(i, j, board[i][j], board)):
                    if (board[i][j] == "O"):
                        oline += 1
                    else:
                        xline += 1
            if i == 2 and j == 0:
                if (isY(i, j, board[i][j], board)):
                    if (board[i][j] == "O"):
                        oline += 1
                    else:
                        xline += 1
    print(O, oline, X, xline)
    # O==X인데 Oline이 더 많거나 같은 경우
    # O>X인데 Xline이 더 많거나 같은 경우
    if (O == X):
        if oline >= xline and oline >= 1:
            return False
    elif (O > X):
        if xline >= oline and xline >= 1:
            return False
    return True


def solution(board):
    ans = -1
    if (game(board)):
        ans = 1
    else:
        ans = 0
    return ans
