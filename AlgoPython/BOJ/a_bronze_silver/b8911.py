'''
문제설명
    명령이 주어졌을 때 거북이가 이동한 영역을 구해라.

구상
    이동할 때마다 최소 최대 x,y를 갱신해서 넓이를 구한다.
    2차원 배열처럼 생겼지만 굳이 그렇게 안해도 된다.

제츌횟수 4회
틀린이유  d = 1 을 d ==1 로 썼음.....

'''
T = int(input())
for tc in range(T):

    order_list = list(input())
    minR, maxR, minC, maxC = 0, -501, 0, -501
    # 북 동 남 서
    row = [1, 0, -1, 0]
    col = [0, 1, 0, -1]
    r, c, d = 0, 0, 0  # 시작점과 방향
    for order in order_list:
        if (order == "F"):
            r = r + row[d]
            c = c + col[d]
        elif (order == "B"):
            r = r - row[d]
            c = c - col[d]
        elif (order == "L"):
            d = (d-1+d)%4
        elif (order == "R"):
            d = (d+1) % 4
        minR = min(minR, r)
        minC = min(minC, c)
        maxR = max(maxR, r)
        maxC = max(maxC, c)
    print(abs(maxR - minR) * abs(maxC - minC))
