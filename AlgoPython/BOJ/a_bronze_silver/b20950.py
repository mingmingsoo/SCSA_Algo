'''
문제 설명
    N개의 행 중 최대 7개를 선택해서
    문두리 색을 구해라

입력
    색깔 갯수
    색깔 정보 N개
    문두리색

출력
    곰도리색 - 문두리색

구상
    부분집합 레추게릿 가능한가요?
    아니요.
    다른 아이디어 있나요?
    아니요.
반례
    10
    1 1 1
    2 2 2
    3 3 3
    4 4 4
    5 5 5
    6 6 6
    7 7 7
    8 8 8
    9 9 9
    10 10 10
    4 4 4
    diff가 0인 sel 을찍어보면 알 수 있음.
'''

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
target = list(map(int, input().split()))
ans = 1000
sel = [0] * n


def subset(idx):
    global ans
    if sel.count(1) > 7:
        return
    if idx == n:
        if sel.count(1) < 2:
            return
        r, g, b = 0, 0, 0
        cnt = sel.count(1)  # 내가 선택한 물감 갯수
        for i in range(n):
            if (sel[i] == 1):
                r += grid[i][0]
                g += grid[i][1]
                b += grid[i][2]
        r //= cnt
        g //= cnt
        b //= cnt
        # print(r,g,b)
        diff_r, diff_g, diff_b = abs(target[0] - r), abs(target[1] - g), abs(target[2] - b)
        diff = diff_r + diff_g + diff_b
        ans = min(ans, diff)
        return

    sel[idx] = 1 # 이게 순서가 바뀌면 안되네...
    subset(idx + 1)
    sel[idx] = 0
    subset(idx + 1)


subset(0)
print(ans)
