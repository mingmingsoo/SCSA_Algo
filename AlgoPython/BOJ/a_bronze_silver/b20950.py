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
found = False


def subset(idx, cnt, r, g, b):
    global ans, found
    if(n-idx+cnt<2):
        return
    if cnt > 7:
        return
    if 2 <= cnt <= 7:

        tmp_r = r // cnt
        tmp_g = g // cnt
        tmp_b = b // cnt

        if (tmp_r == target[0] and tmp_g == target[1] and tmp_b == target[2]):
            found = True
            ans = 0
            return
        else:
            ans = min(ans, abs(target[0] - tmp_r) + abs(target[1] - tmp_g) + abs(target[2] - tmp_b))

    if idx == n:
        return
    # 골랐어
    subset(idx + 1, cnt + 1, r + grid[idx][0], g + grid[idx][1], b + grid[idx][2])
    # 안골랐어
    subset(idx + 1, cnt, r, g, b)


subset(0, 0, 0, 0, 0)
print(ans)
