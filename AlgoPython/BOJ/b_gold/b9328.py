T = int(input())
for tc in range(T):
    '''
    소요시간 1시간 20분
    거 참 재밌네
    
    bfs 
    1. . 들만 갈 수 있음
    2. 대문자 만났는데 내가 동일한 소문자 있으면 그 곳을 .으로 바꿈(얘는 유지)
    3. 달러 있으면 냠냠 굿 하고 .으로 바꿈(얘도 유지)
    4. 소문자 만나면 먹어!
    5. 이야 근데 이거 visted 를 어케하지..

    -> 열쇠랑 문서를 먹을때마다 visted를 초기화해준다!

    '''
    from collections import deque

    n, m = map(int, input().split())

    grid = [list(input()) for i in range(n)]
    # 패딩
    grid.insert(0, ["."] * m)
    grid.append(["."] * m)
    for row in grid:
        row.insert(0, ".")
        row.append(".")

    n += 2
    m += 2

    key = set(input())
    q = deque([])
    document = 0
    visited = [[False] * m for i in range(n)]

    # 초기 셋팅. 주변 가장자리 중 입구 넣어주고.
    # 문인데 키가 있는 애들은 . 처리 해줌
    # 가장자리의 열쇠들 냠냠해줌.

    for i in range(1, n, n - 3):
        for j in range(1, m - 1):
            if (grid[i][j] == "."):
                q.append((i, j))
                visited[i][j] = True
            # 문인데 내가 열쇠가 있으면 .로 변경
            elif ("A" <= grid[i][j] <= "Z" and chr(ord(grid[i][j]) + 32) in key):
                q.append((i, j))
                grid[i][j] = "."
                visited[i][j] = True
            # 열쇠 .로 변경
            elif ("a" <= grid[i][j] <= "z"):
                if(grid[i][j] not in key):
                    key.add(grid[i][j])
                q.append((i, j))
                grid[i][j] = "."
                visited[i][j] = True
    for i in range(2, n - 2):
        for j in range(1, m, m - 3):
            if (grid[i][j] == "."):
                q.append((i, j))
                visited[i][j] = True
            elif ("A" <= grid[i][j] <= "Z" and chr(ord(grid[i][j]) + 32) in key):
                q.append((i, j))
                grid[i][j] = "."
                visited[i][j] = True
            elif ("a" <= grid[i][j] <= "z"):
                if(grid[i][j] not in key):
                    key.add(grid[i][j])
                q.append((i, j))
                grid[i][j] = "."
                visited[i][j] = True

    # print(q)
    # print("---------------")
    # for row in grid:
    #     print(*row)

    # if (not q):  # 입구조차 없으면 시작 안해도됨
    #     print(0)
    #     exit()

    def bfs():
        global document, visited
        row = [-1, 1, 0, 0]
        col = [0, 0, 1, -1]
        while q:
            r, c = q.popleft()

            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if (not (0 <= nr < n and 0 <= nc < m)):
                    continue

                if (not visited[nr][nc] and grid[nr][nc] == "."):
                    q.append((nr, nc))
                    visited[nr][nc] = True

                if ("A" <= grid[nr][nc] <= "Z"):  # 문인데
                    if (chr(ord(grid[nr][nc]) + 32) in key):  # 열쇠가 있으면 갈 수 있음
                        grid[nr][nc] = "."
                        q.append((nr, nc))
                        visited = [[False] * m for i in range(n)]  # visted 초기화

                if ("a" <= grid[nr][nc] <= "z"):  # 열쇠인데 새 열쇠면 넣어준다. 그리고 갈 수 있다.
                    if(grid[nr][nc] not in key):
                        key.add(grid[nr][nc])
                    grid[nr][nc] = "."
                    q.append((nr, nc))
                    visited = [[False] * m for i in range(n)]  # visted 초기화

                if (grid[nr][nc] == "$"): # 문서 냠냠
                    document += 1
                    grid[nr][nc] = "."
                    visited = [[False] * m for i in range(n)]  # visted 초기화
                    q.append((nr,nc))


    bfs()
    print(document)
    # print(key)

