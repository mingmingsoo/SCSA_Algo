n, order_num = map(int, input().split())

r, c = 0, 0
d = 3  # 동쪽
row = [-1, 0, 1, 0]
col = [0, -1, 0, 1]

for i in range(order_num):
    tmp = list(input().split())
    # print(r, c, d)
    if tmp[0] == "MOVE":
        how = int(tmp[1])
        if 0 <= r + row[d] * how < n and 0 <= c + col[d] * how < n:
            r = r + row[d] * how
            c = c + col[d] * how
        else:
            print(-1)
            exit()
    else:
        how = int(tmp[1])
        if (how == 0):
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
print(c,r)
