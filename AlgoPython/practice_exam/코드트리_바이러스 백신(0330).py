'''
# 코드트리 바이러스 백신
2025.03.30.일
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 14:49
    1차 제출  15:01
    문제 종료 15:02

    총 풀이시간 13분
        49~52   : 문제 이해(3)
        52~54   : combi 작성(2)
        54~01   : bfs 작성(7)
                    1.(0 < nc < n) 부등호 빠져있어서 수정 (0 <= nc < n)
                    2. ans = -1 이여서 최솟값 갱신이 안되네.. ans 수정!
        01~02   : 답이 0일때 -1 이 나옴
                    maxi를 -1로 초기화해서,,ㅠㅠ maxi 0으로 수정!

  메모리 18 MB
  시간 67 ms

  회고
    1. 틀린이유 maxi 를 -1로 초기화해서 생긴 오류
        maxi 는 0으로 초기화 시켜줘야함..
        초기화 생각하고 해!!!!!!!!!!!!!!!!


# 문제 풀면서의 기록
combi+bfs
시간복잡도
총병원 10 개 선택하는 병원 m개
bfs 50*50
10Cm * 50*50 ㄱㅊ

'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            arr.append((i, j))

sel = [0] * m
ans = 50*50+1

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def combi(sidx, idx):
    global ans
    if sidx == m:
        # 주의할 점이 선택한 병원으로 퍼져나가는데
        # 시간 갱신은 병원이 아닌 곳으로 해야함.
        visited = [[False] * n for i in range(n)]
        q = deque()
        for r, c in sel:
            visited[r][c] = True
            q.append((r, c, 0))

        maxi = 0
        while q:
            r, c, time = q.popleft()
            if grid[r][c] == 0:
                maxi = time
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] == 1 or visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc, time + 1))

        isok = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    isok = False
                    break
            if not isok:
                break
        if isok:
            ans = min(ans, maxi)

        return

    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
if ans == 2501:
    print(-1)
else:
    print(ans)