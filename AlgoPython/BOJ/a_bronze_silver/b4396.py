n = int(input())

bombGrid = [list(input()) for i in range(n)]
currGrid = [list(input()) for i in range(n)]

row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]
ansGrid = [["."] * n for i in range(n)]


# 근방 지뢰 갯수를 확인해서 출력해야 하는 배열에 적용하는 로직
def isCnt():
    for i in range(n):
        for j in range(n):
            if (currGrid[i][j] == 'x'):
                sum = 0
                for k in range(8):
                    ni = i + row[k]
                    nj = j + col[k]
                    if (0 <= ni < n and 0 <= nj < n and bombGrid[ni][nj] == '*'):
                        sum += 1
                ansGrid[i][j] = sum


# 지뢰를 눌렀다면 지뢰를 적용해주는 로직
def isBomb():
    for i in range(n):
        for j in range(n):
            if (bombGrid[i][j] == "*" and currGrid[i][j] == "x"):
                return True
    return False


isCnt()

if (isBomb()):
    for i in range(n):
        for j in range(n):
            if (bombGrid[i][j] == "*"):
                ansGrid[i][j] = "*"

# 출력
for i in range(n):

    for j in range(n):
        print(ansGrid[i][j], end="")
    print()