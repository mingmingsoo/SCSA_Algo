'''
dict 사용한 두번째 풀이
열이 영어, 행이 숫자.
'''
orders = {"R": (0, 1), "L": (0, -1), "B": (-1, 0), "T": (1, 0), "RT": (1, 1), "LT": (1, -1), "RB": (-1, 1),
          "LB": (-1, -1)}
tmpK, tmpS, n = input().split()
c, r, sc, sr, n = ord(tmpK[0]) - 65, int(tmpK[1]) - 1, ord(tmpS[0]) - 65, int(tmpS[1]) - 1, int(n)
for _ in range(n):
    order = input()
    dir = orders[order]
    nr = r + dir[0]
    nc = c + dir[1]

    nsr = sr + dir[0]
    nsc = sc + dir[1]
    if (0 <= nr < 8 and 0 <= nc < 8):
        if (nr == sr and nc == sc):
            if (0 <= nsr < 8 and 0 <= nsc < 8):
                r, c, sr, sc = nr, nc, nsr, nsc
            else:
                continue
        else:
            r, c = nr, nc
    else:
        continue
print(f"{chr(c + 65)}{r + 1}")
print(f"{chr(sc + 65)}{sr + 1}")
