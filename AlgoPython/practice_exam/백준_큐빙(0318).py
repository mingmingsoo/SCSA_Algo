T = int(input())


def rotation(idx):
    face_ro = [_[:] for _ in cube[idx]]
    for i in range(3):
        for j in range(3):
            cube[idx][i][j] = face_ro[2 - j][i]


def up():
    rotation(0)
    f1, f2, f3 = cube[2][0][0], cube[2][0][1], cube[2][0][2]
    cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2]  # 오
    cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[3][0][0], cube[3][0][1], cube[3][0][2]  # 뒤
    cube[3][0][0], cube[3][0][1], cube[3][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]  # 왼
    cube[4][0][0], cube[4][0][1], cube[4][0][2] = f1, f2, f3


def down():
    rotation(1)
    f1, f2, f3 = cube[2][2][0], cube[2][2][1], cube[2][2][2]
    cube[2][2][0], cube[2][2][1], cube[2][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]  # 왼
    cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]  # 뒤
    cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[5][2][0], cube[5][2][1], cube[5][2][2]  # 오
    cube[5][2][0], cube[5][2][1], cube[5][2][2] = f1, f2, f3


def front():
    rotation(2)
    u1, u2, u3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
    cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]  # 왼
    cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][0][2], cube[1][0][1], cube[1][0][0]  # 뒤
    cube[1][0][2], cube[1][0][1], cube[1][0][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
    cube[5][0][0], cube[5][1][0], cube[5][2][0] = u1, u2, u3


def back():
    rotation(3)
    u1, u2, u3 = cube[0][0][2], cube[0][0][1], cube[0][0][0]
    cube[0][0][2], cube[0][0][1], cube[0][0][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]  # 오
    cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[1][2][0], cube[1][2][1], cube[1][2][2]  # 아래
    cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]  # 왼
    cube[4][0][0], cube[4][1][0], cube[4][2][0] = u1, u2, u3


def left():
    rotation(4)
    u1, u2, u3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
    cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
    cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
    cube[2][0][0], cube[2][1][0], cube[2][2][0] = u1, u2, u3


def right():
    rotation(5)
    u1, u2, u3 = cube[0][2][2], cube[0][1][2], cube[0][0][2]
    cube[0][2][2], cube[0][1][2], cube[0][0][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
    cube[2][2][2], cube[2][1][2], cube[2][0][2] = cube[1][2][2], cube[1][1][2], cube[1][0][2]  # 아래
    cube[1][2][2], cube[1][1][2], cube[1][0][2] = cube[3][0][0], cube[3][1][0], cube[3][2][0]  # 뒤
    cube[3][0][0], cube[3][1][0], cube[3][2][0] = u1, u2, u3


for tc in range(T):
    '''
    그냥 .. 내 방식대로 풀자..........
    '''
    color = ["w", "y", "r", "o", "g", "b"]
    cube = []
    for c in color:
        grid = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                grid[i][j] = c
        cube.append(grid)

    # for row in cube:
    #     for col in row:
    #         print(*col)

    func_dict = {"U": up, "D": down, "F": front, "B": back, "L": left, "R": right}
    _ = input()
    order_lst = list(input().split())
    for order in order_lst:
        f, d = order
        if d == "-":
            d = 3
        else:
            d = 1

        for dd in range(d):
            func_dict[f]()

    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end="")
        print()


'''
# 백준 5373 큐빙
# 체감난이도 플5이 맞다. 하드코딩 안하는 법이 생각이 안남 respect 준영

# 문제 풀고 나서 기록

    문제 시작 09:00
    1차 제출  10:12
    문제 종료 10:18
    총 풀이시간 78분
        00~04   : 큐브 만들기(4) (자바였으면 for문 돌렸겠지만 god 파이썬이라 직접 만듬)
        04~12   : 로직 작성(68)
        12      : 틀렸습니다
        12~18   : 면 마다 잘 돌아가는지 확인(6) <- 이걸 내기 전에 했어야지 이 사람아
                  F+ 일때 이상한 거 확인 -> 수정

    1차
    메모리 116632 KB
    시간 236 ms
    2차
    메모리 113864 KB
    시간 308 ms

    회고
        1. 이런 문제는 집중이 잠깐 흐트러져도 로직이 틀린다.......
            한번 놓쳤으면 싹 지우고 새로해야함 ㅠ
            하드 코딩 안한 코드를 살펴보자.............!!!!!!!!!!!!!!!!!!!!!!!
        2. 앞면 회전이 틀려서 1회 틀렸는데. 아쉽다... F+ B+ 이 잘 나오길래 넘어갔는데
            F+만 해볼걸 그랬다.
        3. 새로 안 사실
            dict에 함수도 넣을 수 있다. 다만 주의할 점!!
            *************************************************
            rotation_dict = {"U": up()}
            rotation_dict["U"] 이 아님!!!
            *************************************************
            rotation_dict = {"U": up}
            rotation_dict["U"]() 이렇게 하면 된다!!!
            즉 dict에 함수 명을 써주고 호출할 때 dict[key]() 이렇게!
            *************************************************

# 문제 풀면서의 기록
1
1
L+

1
1
R-

1
1
B-


1
1
F- # 이거 이상

1
1
U+
'''

#######################################################################
# 코드 리팩토링, 함수화 & dict
def face_rotation(f):
    face = [_[:] for _ in cube[f]]
    for i in range(3):
        for j in range(3):
            cube[f][i][j] = face[3 - j - 1][i]  # 시계 면


def up():
    face_rotation(0)
    f1, f2, f3 = cube[2][0][0], cube[2][0][1], cube[2][0][2]
    cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
    cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
    cube[3][0][0], cube[3][0][1], cube[3][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
    cube[4][0][0], cube[4][0][1], cube[4][0][2] = f1, f2, f3


def down():
    face_rotation(1)
    f1, f2, f3 = cube[2][2][0], cube[2][2][1], cube[2][2][2]
    cube[2][2][0], cube[2][2][1], cube[2][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]  # 앞 왼
    cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]  # 왼 뒤
    cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[5][2][0], cube[5][2][1], cube[5][2][2]  # 뒤 오
    cube[5][2][0], cube[5][2][1], cube[5][2][2] = f1, f2, f3  # 오 앞


def front():
    face_rotation(2)
    u1, u2, u3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
    cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]  # 위 왼
    cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][0][2], cube[1][0][1], cube[1][0][0]  # 왼 밑
    cube[1][0][2], cube[1][0][1], cube[1][0][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]  # 밑 오
    cube[5][0][0], cube[5][1][0], cube[5][2][0] = u1, u2, u3  # 오 위


def back():
    face_rotation(3)
    u1, u2, u3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
    cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]  # 위 뒤
    cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]  # 뒤 밑
    cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[4][2][0], cube[4][1][0], cube[4][0][0]  # 밑 앞
    cube[4][2][0], cube[4][1][0], cube[4][0][0] = u1, u2, u3  # 앞 위


def left():
    face_rotation(4)
    u1, u2, u3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]  # 위 뒤
    cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]  # 뒤 밑
    cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]  # 밑 앞
    cube[2][0][0], cube[2][1][0], cube[2][2][0] = u1, u2, u3  # 앞 위


def right():
    face_rotation(5)
    u1, u2, u3 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
    cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]  # 위 앞
    cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]  # 앞 밑
    cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]  # 밑 뒤
    cube[3][2][0], cube[3][1][0], cube[3][0][0] = u1, u2, u3  # 뒤 위


rotation_dict = {"U": up, "D": down, "F": front, "B": back, "L": left, "R": right}
T = int(input())
for tc in range(T):
    cube = [[["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],  # 위 0
            [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],  # 밑 1
            [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],  # 앞 2
            [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]],  # 뒤 3
            [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],  # 왼 4
            [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]]]  # 오 5

    order_num = int(input())
    order_list = list(input().split())
    for order in order_list:
        face, d = order[0], order[1]
        if d == "+": d = 1
        else: d = 3
        for i in range(d):
            rotation_dict[face]()
    for _ in cube[0]:
        print("".join(_))
#######################################################################
# 첫번째 풀이
T = int(input())
for tc in range(T):
    cube = [[["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],  # 위 0
            [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],  # 밑 1
            [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],  # 앞 2
            [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]],  # 뒤 3
            [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],  # 왼 4
            [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]]]  # 오 5

    order_num = int(input())
    order_list = list(input().split())


    def up_rotation():
        # 일단 시계
        face = [_[:] for _ in cube[0]]
        for i in range(3):
            for j in range(3):
                cube[0][i][j] = face[3 - j - 1][i]  # 시계 면

        f1, f2, f3 = cube[2][0][0], cube[2][0][1], cube[2][0][2]
        cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = f1, f2, f3


    # ok

    def down_rotation():
        # 일단 시계
        face = [_[:] for _ in cube[1]]
        for i in range(3):
            for j in range(3):
                cube[1][i][j] = face[3 - j - 1][i]  # 시계 면

        f1, f2, f3 = cube[2][2][0], cube[2][2][1], cube[2][2][2]
        cube[2][2][0], cube[2][2][1], cube[2][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]  # 앞 왼
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]  # 왼 뒤
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[5][2][0], cube[5][2][1], cube[5][2][2]  # 뒤 오
        cube[5][2][0], cube[5][2][1], cube[5][2][2] = f1, f2, f3  # 오 앞


    # ok

    def front_rotation():
        face = [_[:] for _ in cube[2]]
        for i in range(3):
            for j in range(3):
                cube[2][i][j] = face[3 - j - 1][i]  # 시계 면

        u1, u2, u3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]  # 위 왼
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][0][2], cube[1][0][1], cube[1][0][0]  # 왼 밑
        cube[1][0][2], cube[1][0][1], cube[1][0][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]  # 밑 오
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = u1, u2, u3  # 오 위


    # ok

    def back_rotation():
        face = [_[:] for _ in cube[3]]
        for i in range(3):
            for j in range(3):
                cube[3][i][j] = face[3 - j - 1][i]  # 시계 면

        u1, u2, u3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
        cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]  # 위 뒤
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]  # 뒤 밑
        cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[4][2][0], cube[4][1][0], cube[4][0][0]  # 밑 앞
        cube[4][2][0], cube[4][1][0], cube[4][0][0] = u1, u2, u3  # 앞 위


    def left_rotation():  # ok
        face = [_[:] for _ in cube[4]]
        for i in range(3):
            for j in range(3):
                cube[4][i][j] = face[3 - j - 1][i]  # 시계 면

        u1, u2, u3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]  # 위 뒤
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]  # 뒤 밑
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]  # 밑 앞
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = u1, u2, u3  # 앞 위


    # ok

    def right_rotation():
        face = [_[:] for _ in cube[5]]
        for i in range(3):
            for j in range(3):
                cube[5][i][j] = face[3 - j - 1][i]  # 시계 면

        u1, u2, u3 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]  # 위 앞
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]  # 앞 밑

        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]  # 밑 뒤
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = u1, u2, u3  # 뒤 위


    # ok

    for order in order_list:
        face, d = order[0], order[1]
        if face == "U":
            if d == "+":
                up_rotation()
            else:
                up_rotation()
                up_rotation()
                up_rotation()
        elif face == "D":
            if d == "+":
                down_rotation()
            else:
                down_rotation()
                down_rotation()
                down_rotation()
        elif face == "F":
            if d == "+":
                front_rotation()
            else:
                front_rotation()
                front_rotation()
                front_rotation()
        elif face == "B":
            if d == "+":
                back_rotation()
            else:
                back_rotation()
                back_rotation()
                back_rotation()
        elif face == "L":
            if d == "+":
                left_rotation()
            else:
                left_rotation()
                left_rotation()
                left_rotation()
        elif face == "R":
            if d == "+":
                right_rotation()
            else:
                right_rotation()
                right_rotation()
                right_rotation()

    for _ in cube[0]:
        print("".join(_))
