'''

문제 설명
    한 이닝에 3아웃 발생시 종료-> 공 수 변경
    타순정한다.
    9번까지 공쳤는데 3아웃 없으면 1타자가 다시 타석에 선다.
    이닝 변경해도 순서는 유지 -> 순서인덱스 필요
    홈 도착시 1점
    1번 선수가 4번타자 == 0번 선수가 4번타자

구상
    순열
    구현
'''
import sys

from collections import deque

input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
# 열이 선수 번호.

sel = [0] * 9  # 순서는 순열
visited = [False] * 9
ans = 0


def perm(idx):
    global ans
    if idx == 9:
        score = 0
        player_idx = 0  # 몇번째 선수까지 했냐를 나타냄
        for i in range(n):
            if (n - i) * 24 + score < ans:
                return
            out = 0
            one,two,three = 0,0,0
            while True:
                player = sel[player_idx]  # 선수 번호
                ball = grid[i][player]  # 무슨 공을 칠건지
                if ball == 0:
                    out += 1
                elif ball == 1:
                    score += three
                    three,two,one = two,one,1

                elif ball == 2:
                    score += two + three
                    three, two, one = one, 1, 0

                elif ball == 3:
                    score += one +two +three
                    three, two, one = 1, 0, 0

                else:
                    score += one +two +three +1
                    three, two, one = 0, 0, 0
                player_idx = (player_idx + 1) % 9
                if out >= 3:
                    break
        ans = max(ans, score)
        return

    for i in range(0, 9):
        if not visited[i]:
            if idx == 3 and i != 0:
                continue
            visited[i] = True
            sel[idx] = i
            perm(idx + 1)
            visited[i] = False

perm(0)
print(ans)
