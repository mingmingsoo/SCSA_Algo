n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
r, c = -1, -1
monster_dict = {}
num = 1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "p":
            r, c = i, j
            grid[i][j] = "."
        elif grid[i][j] == "m":
            grid[i][j] = num
            num += 1
mn = int(input())
mtmp = [list(map(int, input().split())) for i in range(3)]

for j in range(mn):
    mhp = mtmp[0][j]
    mdefense = mtmp[1][j]
    mexp = mtmp[2][j]
    monster_dict[j + 1] = [mhp, mdefense, mexp]

on = int(input())
order_lst = list(input().split())

power = 5  # 공격력
power_len = 1  # 공격 사거리
fast = 1  # 이동속도
need_exp = 10  # 요구 경험치
exp = 0  # 경험치
lv = 1  # 레벨
used = 0  # 행동력
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
drug = 0
overdose = False
overdose_used = 0


def attack(d):
    global exp
    # 공격 사거리만큼 한칸씩
    for l in range(1, power_len + 1):
        nr = r + row[d] * l
        nc = c + col[d] * l
        if type(grid[nr][nc]) == int:
            mhp, mdefense, mexp = monster_dict[grid[nr][nc]]
            if power >= mdefense:
                mhp = max(0, mhp - (power - mdefense))
                monster_dict[grid[nr][nc]][0] = mhp
                if mhp == 0:
                    grid[nr][nc] = "."
                    exp += mexp  # 경험치 정리 필요
        elif grid[nr][nc] == "*":
            break


for order in order_lst:
    if order in "udlr":
        d = "udlr".index(order)
        nr = r + row[d] * fast
        nc = c + col[d] * fast
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] in (".", "g"):
            r = nr
            c = nc
            used += 1
            if overdose:
                overdose_used += 1
    elif order == "w":
        used += 1
        if overdose:
            overdose_used += 1
    elif order in ("au", "ad", "al", "ar") and not overdose:  # 공격
        used += 3
        d = "udlr".index(order[1])
        attack(d)
    elif order == "du" and not overdose:  # 약먹기 이동속도 1증가
        used += 2
        fast += 1
        drug += 1  # 이거 처리 필요
    elif order == "dd" and not overdose:  # 약먹기 이동속도 1감소
        used += 2
        fast = max(0, fast - 1)
        drug += 1  # 이거 처리 필요
    elif order == "c" and not overdose:  # 클리어
        if grid[r][c] == "g":
            break

    # 경험치 정리
    if exp >= need_exp:
        while exp >= need_exp:
            exp -= need_exp
            power += lv
            power_len += 1
            need_exp += 10
            lv += 1

    # 약 처리
    if drug >= 5:
        overdose = True
        drug = 0
    if overdose and overdose_used >= 10:
        overdose = False
        overdose_used = 0

print(lv, exp)
print(used)
grid[r][c] = "p"
for i in range(n):
    for j in range(m):
        if type(grid[i][j]) == int:
            print("m", end="")
        else:
            print(grid[i][j], end="")
    print()

ans = []
for i in range(n):
    for j in range(m):
        if type(grid[i][j]) == int:
            ans.append(monster_dict[grid[i][j]][0])
if ans:
    print(*ans)
