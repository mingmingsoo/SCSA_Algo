"""
문제 설명
    1. 선우 이동
    2. 상혁 이동
        4방에 선우 있으면 끝

    visited 배열을 A,B 두가지 다 담으려고 해서 시간초과 났다
    내 생각에는 A가 와리가리 하다보면 B를 마주칠 수 있지 않을까? 했는데
    A가 맵을 한번 탐색 하고나서 B를 못마주쳤으면, 그 후에도 마주칠 수가 없다 그래서 visited를 2차원 배열로만 만들어도 된다는 뜻,....
    완진이 오빠 설명듣고 이해 됐는데 100푸로는 아님


"""
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
ar, ac, br, bc = -1, -1, -1, -1
d = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "B":
            br, bc = i, j
            grid[i][j] = "."
            if i == 0:
                d = 0
            elif j == m - 1:
                d = 1
            elif i == n - 1:
                d = 2
            elif j == 0:
                d = 3
        elif grid[i][j] == "A":
            ar, ac = i, j
            grid[i][j] = "."

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
# B 도는거 미리 만들어놓기
b_location = [(br, bc)]
cnt = 1
total = 2 * n + 2 * (m - 2)
while cnt <= total:
    nr = br + row[d]
    nc = bc + col[d]
    if not (0 <= nr < n and 0 <= nc < m):
        d = (d + 1) % 4
    br += row[d]
    bc += col[d]
    b_location.append((br, bc))
    cnt += 1
b_location.pop()
idx = 0
ans = -1


def bfs(sbr, sbc, sar, sac):
    global ans
    q = deque([(1, sar, sac, 0)])  # 선우 위치, 상혁이 위치, 시간
    visited = [[False] * m for i in range(n)]
    visited[sar][sac] = True
    while q:
        bidx, ar, ac, time = q.popleft()
        br, bc = b_location[bidx]

        for k in range(4):
            nar = ar + row[k]
            nac = ac + col[k]
            if 0 <= nar < n and 0 <= nac < m and grid[nar][nac] != "G" and not visited[nar][nac]:
                if (nar, nac) == (br, bc): # 만났다
                    ans = time + 1
                    return
                else:
                    visited[nar][nac] = True
                    q.append(((bidx + 1) % len(b_location), nar, nac, time + 1))


bfs(br, bc, ar, ac)
print(ans)
