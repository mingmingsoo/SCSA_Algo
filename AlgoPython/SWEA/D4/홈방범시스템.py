'''
문제 설명
    - 손해를 보지 않는 한 최대한 많은 집의 갯수는?
구상
    - 최대한 많이 이므로 대각선을 큰
    - bfs 로 돌리겠다.
패딩을 준다!

왜 헛짓거리를 하는겨 시간초과 나서 범위 따라 완탐함.
'''
T = int(input())

for tc in range(T):

    n, pay = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]

    ans = 0

    for i in range(n):
        for j in range(n):
            for l in range(2 * n, -1, -1):
                ele = 0
                for r in range(n):
                    for c in range(n):
                        if abs(i - r) + abs(j - c) < l and grid[r][c] == 1:
                            ele += 1
                if ele <= ans:
                    break
                cost = (l) * (l) + (l - 1) * (l - 1)
                if ele * pay - cost >= 0:
                    ans = max(ans, ele)

    print(f"#{tc + 1} {ans}")
