'''
돌아오는데에도 시간이 걸림
그게 아니라 손가락이 이동하는 거였음
진짜 자음 모음 따로 치나??
'''

grid = [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        ["a", "s", "d", "f", "g", "h", "j", "k", "l", "-"],
        ["z", "x", "c", "v", "b", "n", "m", "-", "-", "-"]]

left, right = input().split()
sr, sc, er, ec = -1, -1, -1, -1
for i in range(3):
    for j in range(10):
        if (grid[i][j] == left):
            sr, sc = i, j
        elif (grid[i][j] == right):
            er, ec = i, j

order = input()
ans = 0


def find(s):
    for i in range(3):
        for j in range(10):
            if (grid[i][j] == s):
                r, c = i, j
                return r, c


for s in order:
    r, c = find(s)

    if(s in "qwertasdfgzxcv") :
        real_dist = abs(sr - r) + abs(sc - c)
        sr = r
        sc = c
    else:
        real_dist = abs(er - r) + abs(ec - c)
        er = r
        ec = c

    ans += 1
    ans += real_dist
print(ans)
