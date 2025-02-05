'''
빙고!
문제 그대로 구현했습니다...

'''

grid = [list(map(int, input().split())) for i in range(5)]
order = [list(map(int, input().split())) for i in range(5)]

def delete(grid, num): # 불려진 숫자에 따라 0으로 바꿔줌
    for i in range(5):
        for j in range(5):
            if(grid[i][j]==num):
                grid[i][j] = 0
                return

def isbingo():
    line = 0
    # 가로 확인
    for i in range(5):
        isKaro = True
        for j in range(5):
            if(grid[i][j]!=0):
                isKaro = False
                break
        if(isKaro):
            line+=1
    # 세로확인
    for j in range(5):
        isSero = True
        for i in range(5):
            if(grid[i][j]!=0):
                isSero = False
                break
        if(isSero):
            line+=1

    # 대각선1
    isX = True
    for ij in range(5):
          if(grid[ij][ij]!=0):
            isX = False
            break
    if(isX):
        line+=1

    # 대각선2
    isY = True
    for ij in range(5):
          if(grid[ij][5-ij-1]!=0):
            isY = False
            break
    if(isY):
        line+=1
    if(line>=3):
        return True

def bingo():
    # order 순서대로 숫자 말할거임
    for i in range(5):
        for j in range(5):
            num = order[i][j]
            delete(grid,num) # 해당 숫자 지우기
            if(isbingo()): # 0으로 나열된 숫자가 3줄 이상인지 확인
                print(i*5+j+1) # 몇번째?
                return

bingo()

