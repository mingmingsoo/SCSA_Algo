'''
두번째 풀이: min, max 안쓰고 배열에 담기
문제 설명
    F: 직진
    B: 후진
    L: 왼 90
    R: 우 90
    거북이가 지나간 넓이는? -> min,max 갱신해야함
    처음 방향 북쪽
'''
row = [0, 1, 0, -1]  # 북동남서 시계방향
col = [-1, 0, 1, 0]
T = int(input())
for tc in range(T):

    r, c, d = 0, 0, 0
    x = [0]
    y = [0]
    min_r, max_r, min_c, max_c = 0, 0, 0, 0
    order = input()

    for s in order:
        if s == "F":
            r = r + row[d]
            c = c + col[d]
        elif s == "B":
            r = r - row[d]
            c = c - col[d]
        elif s == "L":
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
        x.append(r)
        y.append(c)

    print(abs(max(x) - min(x)) * abs(max(y) - min(y)))
