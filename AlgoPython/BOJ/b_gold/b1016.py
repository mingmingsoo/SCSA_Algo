n, money, start_money, gn = map(int, input().split())
gold_lst = [list(map(int, input().split())) for i in range(gn)]
grid = [[0] * n for i in range(n)]
grid[n - 1][n - 1] = "ST"
grid[n - 1][0] = "MU"
grid[0][0] = "SA"
grid[0][n - 1] = "WU"
r, c = n - 1, n - 2
row = [0, -1, 0, 1]
col = [-1, 0, 1, 0]
d = 0
location = [(n - 1, n - 2)]
for _ in range(4 * n - 8):
    tmp = list(input().split())
    if tmp[0] == "G":
        grid[r][c] = "G"
    else:
        grid[r][c] = int(tmp[1])
    r += row[d]
    c += col[d]
    location.append((r, c))
    if (r, c) == (0, 0) or (r, c) == (n - 1, 0) or (r, c) == (0, n - 1):
        d = (d + 1) % 4
        r += row[d]
        c += col[d]
        location.append((r, c))

social_money = 0
dn = int(input())
dice = [list(map(int, input().split())) for i in range(dn)]

idx = -1
didx = 0
gidx = 0
early_end = False
len_dice = len(dice)
while didx < len_dice:

    d1, d2 = dice[didx]
    go = d1 + d2
    for g in range(go - 1):
        idx = (idx + 1) % (4 * n - 4)
        r, c = location[idx]
        if grid[r][c] == "ST":
            money += start_money

    # 마지막 한 칸: 도착하는 칸
    idx = (idx + 1) % (4 * n - 4)
    r, c = location[idx]
    if grid[r][c] == "ST":
        money += start_money
    elif grid[r][c] == "MU":

        if didx + 1 < dn:
            d1a, d2a = dice[didx + 1]
            if d1a == d2a:
                didx += 2
                continue
        if didx + 2 < dn:
            d1a, d2a = dice[didx + 2]
            if d1a == d2a:
                didx += 3
                continue
        if didx + 3 < dn:
            d1a, d2a = dice[didx + 3]
            if d1a == d2a:
                didx += 4
                continue
        if didx + 4 < dn:  # 위에서  컨티뉴안됐으면..
            didx += 4
            continue

    elif grid[r][c] == "SA":
        money += social_money
        social_money = 0
    elif grid[r][c] == "WU":
        idx = -1
        money += start_money
    elif grid[r][c] == "G":
        ty, order = gold_lst[gidx]
        if ty == 1:
            money += order
        elif ty == 2:
            money -= order  # 여기서 끝나는 거 검사
            if money < 0:
                early_end = True
                break
        elif ty == 3:
            social_money += order
            money -= order  # 여기서 끝나는 거 검사
            if money < 0:
                early_end = True
                break
        elif ty == 4:
            dice.insert(didx + 1, [order, 0])
            len_dice = len(dice)
        gidx = (gidx + 1) % gn
    else:
        r, c = location[idx]
        if grid[r][c] and money >= grid[r][c]:
            money -= grid[r][c]
            grid[r][c] = 0
    didx += 1
if early_end:
    print("LOSE")
else:
    ans = "WIN"
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in ("ST", "MU", "SA", "WU", "G") and grid[i][j]:
                ans = "LOSE"
                break
        if ans == "LOSE":
            break
    print(ans)
