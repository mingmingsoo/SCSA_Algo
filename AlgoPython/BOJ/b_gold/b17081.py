# 만약에 장신구 착용 안하면 어케되는건데 ? 그대로 B야?이동할 수 는 있는거야?
# 착용 안하면 버리는거야?
n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
bn = mn = 0
sr, sc = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] in ("&", "M"):
            mn += 1
        elif grid[i][j] == "B":
            bn += 1
        elif grid[i][j] == "@":
            sr, sc = i, j
            grid[i][j] = "."

tmp = list(input())  # 방향 커맨드
order_lst = []
for o in tmp:
    order_lst.append("URDL".index(o))
moster_dict = {}
for _ in range(mn):
    r, c, name, w, a, h, e = input().split()
    r, c, w, a, h, e = int(r), int(c), int(w), int(a), int(h), int(e)
    if grid[r - 1][c - 1] == "M":
        moster_dict[(r - 1, c - 1)] = [name, w, a, h, e, True]
    else:
        moster_dict[(r - 1, c - 1)] = [name, w, a, h, e, False]

box_dict = {}
for _ in range(bn):
    r, c, type, plus = input().split()
    r, c = int(r), int(c)
    if type in ("W", "A"):
        box_dict[(r - 1, c - 1)] = (type, int(plus))
    else:
        box_dict[(r - 1, c - 1)] = (type, plus)
my_w = 0  # <- 좌표값, 숫자으로 넣어야겠지,
my_a = 0  # <- 좌표값, 숫자으로 넣어야겠지
my_o = set()  # <- (좌표값, 종류)으로 넣어야겠쥐
ment = "Press any key to continue."
hp, power, defense = 20, 2, 2
max_hp = 20
level = 1
exp = 0  # 경험치
need_exp = level * 5
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
r, c = sr, sc
mywin = True
turn = len(order_lst)
for t, d in enumerate(order_lst):
    mywin = True
    nr = r + row[d]
    nc = c + col[d]
    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "#":
        r = nr
        c = nc
    if grid[r][c] == "^":
        if "DX" in my_o:
            hp = max(0, hp - 1)
        else:
            hp = max(0, hp - 5)
        if hp == 0:  # RE 있는지 검사 -> 사용 후 remove
            if "RE" in my_o:
                my_o.remove("RE")
                r, c = sr, sc
                hp = max_hp
            else:
                mywin = False
                ment = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."
                turn = t + 1
                break
    elif grid[r][c] == "B":
        type, plus = box_dict[(r, c)]
        grid[r][c] = "."  # 일단 무조건 열기는 연다.
        if type == "W":  # 무조건 바꿈
            my_w = plus
        elif type == "A":  # 무조건 바꿈
            my_a = plus
        else:  # 고려해야함
            if len(my_o) < 4 and type not in my_o:
                my_o.add(plus)
    elif grid[r][c] in ("&", "M"):  # 쌈 떠야함..
        mname, mpower, mdefense, mhp, mexp, isboss = moster_dict[(r, c)]
        my_full_power = power + my_w
        my_full_defense = defense + my_a
        cnt = 0
        if isboss and "HU" in my_o:
            hp = max_hp
        while True:
            cur_power = max(1, my_full_power - mdefense)
            if cnt == 0 and "CO" in my_o and "DX" in my_o:
                cur_power = max(1, my_full_power * 3 - mdefense)
            elif cnt == 0 and "CO" in my_o:
                cur_power = max(1, my_full_power * 2 - mdefense)
            mhp = max(0, mhp - cur_power)
            if mhp == 0:
                grid[r][c] = "."  # 쥬금
                break
            cur_power = max(1, mpower - my_full_defense)
            if cnt == 0 and isboss and "HU" in my_o:
                cur_power = 0
            hp = max(0, hp - cur_power)
            if hp == 0:  # 나 쥬금
                mywin = False
                break
            cnt += 1
        if not mywin:  # 내가 죽었으면 끝내
            if "RE" in my_o:
                my_o.remove("RE")
                r, c = sr, sc
                hp = max_hp
            else:
                ment = "YOU HAVE BEEN KILLED BY " + mname+".."
                turn = t + 1
                break

        else:  # 내가 이겼다?
            if "EX" in my_o:
                exp += mexp * 12 // 10
            else:
                exp += mexp
            # 경험치 정리
            if exp >= need_exp:
                level += 1
                exp = 0
                need_exp = 5 * level
                max_hp += 5
                power += 2
                defense += 2
                hp = max_hp
            if "HR" in my_o:
                hp = min(max_hp, hp + 3)
            if isboss:  # 내가 이겼고 보스 물리친거면 끝내
                ment = "YOU WIN!"
                turn = t + 1
                break
if mywin:
    grid[r][c] = "@"
for _ in grid:
    print("".join(_))
print("Passed Turns :", turn)
print("LV :", level)
print(f"HP : {hp}/{max_hp}", )
print(f"ATT : {power}+{my_w}", )
print(f"DEF : {defense}+{my_a}", )
print(f"EXP : {exp}/{need_exp}", )
print(ment)
