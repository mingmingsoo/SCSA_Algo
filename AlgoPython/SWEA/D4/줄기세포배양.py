import heapq
from collections import deque


class Node:
    def __init__(self, r, c, time, cur):
        self.r = r
        self.c = c
        self.time = time
        self.cur = cur

    def __lt__(self, other):
        return self.time > other.time


T = int(input())
for tc in range(T):
    '''
    맵 크기를 어떻게 할 것인가?
    k가 300 이므로 1000씩 하면 될 것 같고
    가운데 위치로 잡기.

    마지막 출력을 위해선 전체 배열을 탐색하는 로직이 필요하기는 함.
    bfs에 들고다닐수는 없음

    '''

    size = 1000
    n, m, k = map(int, input().split())
    grid = [[0] * size for i in range(size)]
    startX = size // 2 - n // 2
    startY = size // 2 - m // 2
    endX = size // 2 + n // 2
    endY = size // 2 + m // 2
    if (n % 2 == 1):
        endX += 1
    if (m % 2 == 1):
        endY += 1
    q = []
    for i in range(startX, endX):
        tmp = list(map(int, input().split()))
        for j in range(startY, endY):
            grid[i][j] = tmp[j - startY]
            if (grid[i][j] > 0):
                heapq.heappush(q, Node(i, j, grid[i][j], 0))
                # 위치, 생명력, 활성화되기전 시간, 활성화 되고나서 얼마나 지났는가
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    limit = 0
    dieQ = deque()
    while q:
        if (limit >= k):
            break
        qSize = len(q)  # 5.5 -1 되는거 확인
        newQ = []
        for s in range(qSize):
            node = heapq.heappop(q)
            r = node.r
            c = node.c
            time = node.time
            curTime = node.cur
            if (curTime < time):
                heapq.heappush(newQ, Node(r, c, time, curTime + 1))
                # 시간이 안지났으면 대기
            elif (curTime == time):  # 시간이 지났으면 확장 가능
                dieQ.append(Node(r, c, time, 1))
                # 확장하는 로직
                for d in range(4):
                    nr = r + row[d]
                    nc = c + col[d]
                    if (nr < 0 or nr >= size or nc < 0 or nc >= size):
                        continue
                    elif (grid[nr][nc] == 0):
                        heapq.heappush(newQ, Node(nr, nc, time, 0))
                        grid[nr][nc] = time
                    elif (grid[nr][nc] == -1):
                        continue
        q = newQ
        if dieQ:
            dieQsize = len(dieQ)
            for dieS in range(dieQsize):
                node2 = dieQ.popleft()
                r, c, time, cur = node2.r, node2.c, node2.time, node2.cur
                if (time == cur):
                    grid[r][c] = -1
                else:
                    dieQ.append(Node(r, c, time, cur + 1))

        limit += 1
        # print("----------")
        # for ele in grid:
        #     print(" ".join(f"{num:2}" for num in ele))
    sum = 0
    for i in range(size):
        for j in range(size):
            if (grid[i][j] > 0):
                sum += 1
    print(f"#{tc + 1} {sum}")
