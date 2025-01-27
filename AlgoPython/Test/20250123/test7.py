for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if ((x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2) or (x2 == p1 and q2 == y1) or (x2 == p1 and y2 == q1)):
        print("c")
    elif ((p2 < x1) or (y1 > q2) or (x2 > p1) or (q1 < y2)):
        print("d")
    elif ((y2 == q1) or (p2 == x1) or (q2 == y1) or (x2 == p1)):
        print("b")
    else:
        print("a")