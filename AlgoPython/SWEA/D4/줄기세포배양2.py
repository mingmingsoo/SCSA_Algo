import heapq
from collections import deque

'''
우선순위큐 대신 리스트로 정렬해서 푼 풀이.
시간복잡도 괜찮으면 이렇게 하는게 나을듯. -> 실제로 이게 더 빠름

문제 설명
1. 시작점을 기준으로 생명력에 따라 무한 증식함.
2. 증식후에, 생명력만큼 살아있고 죽는 과정이 필요함.
-> 무한 증식은 bfs를 사용해 품
-> 죽는 과정은 증식한 좌표를 따로 다른 Q에 담아서 해결함.

'''

class Node: # 정렬을 위해 class 생성
    def __init__(self, r, c, time, cur):
        self.r = r
        self.c = c
        self.time = time
        self.cur = cur

    def __lt__(self, other): # 생명력이 큰 애들 우선임.
        return self.time > other.time


T = int(input())
for tc in range(T):

    size = 700 # k가 최대 300이여서 600정도의 맵이 필요함.
    n, m, k = map(int, input().split())
    grid = [[0] * size for i in range(size)]

    # 중간 지점에 맵을 찍기위한 연산.
    startX = size // 2 - n // 2
    startY = size // 2 - m // 2
    endX = size // 2 + n // 2
    endY = size // 2 + m // 2
    if (n % 2 == 1):
        endX += 1
    if (m % 2 == 1):
        endY += 1
    # 확장할 좌표를 담을 q
    q = []
    for i in range(startX, endX):
        tmp = list(map(int, input().split()))
        for j in range(startY, endY):
            grid[i][j] = tmp[j - startY]
            if (grid[i][j] > 0):
                q.append(Node(i, j, grid[i][j], 0))
                # 위치, 생명력, 진행 시간
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    limit = 0
    dieQ = [] # 죽어야 될 애들을 담을 q
    while q:
        if (limit >= k): # 시간이 다다랐으면 종료
            break
        qSize = len(q)  # q 초기 size 만큼만 진행되야함.
        q.sort() # 생명력 순으로 정렬
        for s in range(qSize):
            node = q.pop(0)
            r = node.r
            c = node.c
            time = node.time
            curTime = node.cur
            if (curTime < time): # 아직 비활성상태면 기다려야함
                q.append(Node(r, c, time, curTime + 1))
            elif (curTime == time):  # 활성화 될 수 있는 시간이 됐으면 확장 가능
                dieQ.append(Node(r, c, time, 1)) # 대신 곧 죽을애들이라 dieQ에 넣어줌
                # 확장하는 로직
                for d in range(4):
                    nr = r + row[d]
                    nc = c + col[d]
                    if (nr < 0 or nr >= size or nc < 0 or nc >= size):
                        continue
                    elif (grid[nr][nc] == 0): # 빈공간으로 확장 가능
                        q.append(Node(nr, nc, time, 0))
                        grid[nr][nc] = time
                    elif (grid[nr][nc] == -1): # 죽은 공간으로는 확장 불가.
                        continue
        if dieQ: # 죽을 애들을 검사
            dieQsize = len(dieQ) # 얘도 초기값만큼만 작동해야함.
            for dieS in range(dieQsize):
                node2 = dieQ.pop(0)
                r, c, time, cur = node2.r, node2.c, node2.time, node2.cur
                if (time == cur): # 죽을 때가 됐으면 죽어!
                    grid[r][c] = -1
                else: # 아니면 활성화 상태 유지.
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
