'''
풀이시간
    21분

문제 설명
    #인곳에 십자가를 겹치지 않게 2개 놓으려고한다. 십자가 최대 넓이는?

출력
    1번 십자가 넓이 * 2번 십자가 넓이

구상
    1.  첫번째 구상
        최대넓이라서 일단 모든 # 에서 최대 넓이 될 수 있는 곳을 찾는다
        그리고 저장해두고 거기를 . 으로 바꿈
        그다음에 두번쨰 십자가를 찾음
        ★ 이러면 최대곱이 안나올 수도 있음

    2. 두번째 구상
        조합으로 두 점을 선택하고. 모든 경우의 수를 따져준다.
        근데 모든 경우의 수 안따지고 bfs로 동시에 퍼지게 하는게 최대곱임.
        (그림그려봐서 알았음)

아쉬운점
    조합까지는 구상한대로 짰는데 최대넓이 구하는 것을 의식의 흐름대로 짰음
    통과했으니 망정이지......... ㅜㅜ 메서드 분리도 안했음.. 아쉬움
'''
################################################################
from collections import deque

def bfs(sel):
    global ans
    q = deque()
    visited = [[False] * m for i in range(n)] # 십자가가 겹치면 안되서 visited 필요

    numbering = 0 # 커지는 십자가에 넘버링 해줄거임 0번 십자가, 1 번십자가
    for r, c in sel:
        visited[r][c] = True # 내가 선택한 위치에 일단 방문쳌
        q.append((r, c, 1, 1, numbering))  # 위치, 넓이, 십자가 길이, 넘버링
        numbering += 1

    max_zero = 0 # 0번 십자가 최대
    max_one = 0 # 1번 십자가 최대

    while q:
        r, c, area, length, num = q.popleft()

        # 최대 넓이 갱신
        if num == 0:
            max_zero = area
        else:
            max_one = area

        # 4가지 방향에서 모두 통과해야 q에 넣어줌
        isOk = True
        for k in range(4):
            nr = r + row[k] * length
            nc = c + col[k] * length
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] != "#":
                # 벗어나거나, 다른 십자가하고 겹치거나, 십자가 위치가 안되면 바로 out
                isOk = False
                break
        if isOk: # 그게 아니면 십자가 확대해주기
            q.append((r, c, area + 4, length + 1, num))

            for k in range(4): # 방문체크도 해주기
                nr = r + row[k] * length
                nc = c + col[k] * length
                visited[nr][nc] = True
        else:
            continue

    ans = max(ans, max_one * max_zero)

def combi(sidx, idx):

    if sidx == 2:
        bfs(sel) # bfs 인 척 하는 bfs 가 아닌
        return


    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combi(sidx+1,idx+1)
    combi(sidx, idx+1)

################################################################
n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
row = [-1,1,0,0]
col = [0,0,1,-1]

arr = [] # 조합을 위한 배열
for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            arr.append((i,j)) # 십자가 가능한 위치 모두 담음

sel = [0]*2 # 내가 선택할 두개의 십자가 위치
ans = 1
combi(0,0)
print(ans)