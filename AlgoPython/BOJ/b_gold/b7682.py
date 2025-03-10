while True:
    '''
    틱텍토
    시작은 무조건X
    성공은 3개의 선 하나라도 있으면

    안되는 조건
    1. X-0는 0또는 1이여야함.
    2. O가 X보다 작은데 O 선이 x선보다 많을 경우
    3. 선이 하나도 없으면

    XXXOOO...
    반례
    '''
    tmp = list(input())
    if tmp == ["e", "n", "d"]:
        break
    x_cnt, o_cnt = tmp.count("X"), tmp.count("O")
    empty = 9 - x_cnt - o_cnt
    grid = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            grid[i][j] = tmp.pop(0)


    def first_valid():
        if x_cnt - o_cnt == 0 or x_cnt - o_cnt == 1:
            return True
        # print("갯수 안맞음")
        return False


    def second_valid():
        x_line, o_line = 0, 0
        # 가로검사
        for i in range(3):
            if grid[i].count("X") == 3:
                x_line += 1
            if grid[i].count("O") == 3:
                o_line += 1

        # 세로검사
        grid_t = list(zip(*grid))
        for i in range(3):
            if grid_t[i].count("X") == 3:
                x_line += 1
            if grid_t[i].count("O") == 3:
                o_line += 1
        # 아래 대각선 검사
        x1, o1 = 0, 0
        for i in range(3):
            if grid[i][i] == "X":
                x1 += 1
            elif grid[i][i] == "O":
                o1 += 1
        if x1 == 3:
            x_line += 1
        elif o1 == 3:
            o_line += 1

        # 위 대각선 검사
        x2, o2 = 0, 0
        for i in range(3):
            if grid[i][2 - i] == "X":
                x2 += 1
            elif grid[i][2 - i] == "O":
                o2 += 1
        if x2 == 3:
            x_line += 1
        elif o2 == 3:
            o_line += 1

        # 1. X-0는 0또는 1이여야함.
        # 2. 두개 선이 1이상인데 갯수 같을 때
        # 3. x가 이겼는데 두개 갯수가 같을 때
        # 2. O가 X보다 작은데 O 선이 x선보다 많을 경우
        # 3. 선이 하나도 없으면
        # print(x_line,o_line)
        if x_line == o_line == 0 and empty > 0:
            # print("게임 종료 안됐음")
            return False
        if x_line == o_line > 0:
            return False
        if x_line > o_line and o_cnt == x_cnt:
            return False
        if o_line and o_line > x_line and o_cnt < x_cnt:
            # print("먼가이상함")
            return False
        return True


    if first_valid() and second_valid():
        print("valid")
    else:
        print("invalid")
