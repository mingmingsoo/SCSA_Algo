T = int(input())
for tc in range(T):
    '''

    bfs 
    1. . 들만 갈 수 있음
    2. 대문자 만났는데 내가 동일한 소문자 있으면 그 곳을 .으로 바꿈(얘는 유지)
    3. 달러 있으면 냠냠 굿 하고 .으로 바꿈(얘도 유지)
    4. 소문자 만나면 먹어!
    5. 이야 근데 이거 visted 를 어케하지..

    -> 열쇠랑 문서를 먹을때마다 visted를 초기화해준다!
    
    쉽게 가보자..
    틀린이유:... 밑에있움
    
    초기 입구를 이것저것 다 따지지 말고
    그냥 쉽게쉽게 가면 맞춤^_^....

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

    for i in range(0,n,n-1):
        for j in range(m):
                q.append((i,j))

    for i in range(1,n-1):
        for j in range(0,m,m-1):
                q.append((i,j))

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

                if (65 <= ord(grid[nr][nc]) <= 90):  # 문인데
                    if (chr(ord(grid[nr][nc]) + 32) in key):  # 열쇠가 있으면 갈 수 있음
                        grid[nr][nc] = "."
                        q.append((nr, nc))
                        visited = [[False] * m for i in range(n)]  # visted 초기화

                if (97 <= ord(grid[nr][nc]) <= 122):  # 열쇠인데 새 열쇠면 넣어준다. 그리고 갈 수 있다.
                    if(grid[nr][nc] not in key):
                        key.add(grid[nr][nc])
                    grid[nr][nc] = "."
                    q.append((nr, nc))
                    visited = [[False] * m for i in range(n)]  # visted 초기화

                if (grid[nr][nc] == "$"): # 문서 냠냠
                    document += 1
                    grid[nr][nc] = "."
                    q.append((nr, nc)) # 와 씨 이게 없어서
                    visited = [[False] * m for i in range(n)]  # visted 초기화


    bfs()
    print(document)

