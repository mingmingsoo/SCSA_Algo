'''
13:48~14:53 (65분)
두번째 풀이 : 굳이 visited 써보기 -> 368 에서 120으로 줄어들었음 굳이가 아니였음
세번쨰 풀이: visited 4차원으로 써보기

문제설명
    10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지?
    왼/오/위/아 기울이기 가능
    1. 파란구슬 빠지면 실패
    2. 빨, 파 동시에 빠져도 실패
    3. 구슬이 움직이지 않으면 그만.
구상
    bfs R과 B 방향을 같이 관리해줘야함.
    O에 도달하면.....
    종료조건을 봐줘야할 듯
오해
    10번이 좌라라라라락 10번이였음. 한칸씩 이동이 아녔음
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

ar, ac, br, bc = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "R":
            ar, ac = i, j
            grid[i][j] = "."
        elif grid[i][j] == "B":
            br, bc = i, j
            grid[i][j] = "."
isOk = False  # 가능하냐?
visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]


def bfs(ar, ac, br, bc):
    global isOk
    q = deque([(ar, ac, br, bc, 0)])  # 빨, 파 같이 관리해줘야함
    # visited 는 쓰지 않는다 써도 되긴하는데..
    row = [0, 1, 0, -1]
    col = [-1, 0, 1, 0]
    while q:
        ar, ac, br, bc, time = q.popleft()
        if grid[ar][ac] == "O" and grid[br][bc] != "O":  # 동시에 들어온게 아니면 탈출 성공
            isOk = True
            return
        if grid[br][bc] == "O":  # 파란거 먼저 들어왔으면 실패 다음 경우의 수
            continue

        if time > 10:
            return  # 기회 끝

        origin_ar, origin_ac, origin_br, origin_bc = ar, ac, br, bc
        # 왼/오/위/아 기울이기 가능
        for k in range(4):
            ar, ac, br, bc = origin_ar, origin_ac, origin_br, origin_bc
            while True:
                # 갈 수 있으면
                anr = ar + row[k]
                anc = ac + col[k]
                if 0 <= anr < n and 0 <= anc < m and grid[anr][anc] == ".":
                    ar = anr
                    ac = anc
                elif 0 <= anr < n and 0 <= anc < m and grid[anr][anc] == "O":
                    ar = anr
                    ac = anc
                    break
                else:
                    break
            while True:
                bnr = br + row[k]
                bnc = bc + col[k]
                # 갈 수 있으면
                if 0 <= bnr < n and 0 <= bnc < m and grid[bnr][bnc] == ".":
                    br = bnr
                    bc = bnc
                elif 0 <= bnr < n and 0 <= bnc < m and grid[bnr][bnc] == "O":
                    br = bnr
                    bc = bnc
                    break
                else:
                    break

            if origin_ar == ar and origin_ac == ac and origin_br == br and origin_bc == bc:
                continue  # 이동이 없었으면 넘어가

            if ar == br and ac == bc and grid[ar][ac] == ".":
                # 만약 같았다면 누가 먼저 왔는지 확인해준다. "O"일때는 아님
                if k == 0:
                    # 서쪽으로 왔을 땐
                    # 오리지널이 c가 큰애가 하나 오른쪽으로
                    if (origin_ac < origin_bc):
                        bc += 1
                    else:
                        ac += 1
                elif k == 1:
                    # 남쪽이면 orign r이 작은 애가 -1 해줌
                    if (origin_ar > origin_br):
                        br -= 1
                    else:
                        ar -= 1
                elif k == 2:
                    # 동쪽이면 orign c이 작은 애가 -1 해줌
                    if (origin_ac > origin_bc):
                        bc -= 1
                    else:
                        ac -= 1
                elif k == 3:
                    # 북쪽이면 orign r이 큰 애가 +1 해줌
                    if (origin_ar < origin_br):
                        br += 1
                    else:
                        ar += 1
            if not visited[ar][ac][br][bc]:
                visited[ar][ac][br][bc] = True
                q.append((ar, ac, br, bc, time + 1))

    # 1. 파란구슬 빠지면 실패
    # 2. 빨, 파 동시에 빠져도 실패
    # 3. 구슬이 움직이지 않으면 그만. o
    # 같은 위치는 불가능 o


bfs(ar, ac, br, bc)
if isOk:
    print(1)
else:
    print(0)
