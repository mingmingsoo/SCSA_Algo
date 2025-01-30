grid = [list(map(int, input().split())) for i in range(5)]

order =[list(map(int, input().split())) for i in range(5)]
def bingo():
    pass


def game():
    for i in range(5):
        for j in range(5):
            num = order[i][j]
            for r in range(5):
                for c in range(5):
                    if (grid[r][c] == num):
                        grid[r][c] = -1
                    if (bingo() >= 3):
                        print(j * 5 + i+1)
                        return


game()

