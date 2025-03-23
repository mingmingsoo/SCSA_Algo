'''
어렵게 접근했는데
tail을 q로 관리하기 가보기
'''
from collections import deque

n = int(input())
grid = [[0] * n for i in range(n)]
apple = int(input())
for i in range(apple):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 2  # 사과
rotation_list = []
rotation_list.sort(reverse=True)
dnum = int(input())
for i in range(dnum):
    t, d = input().split()
    rotation_list.append((int(t), d))

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
time = 0
grid[0][0] = 1  # 뱀


def game():
    global time
    length = 1
    r, c, d = 0, 0, 0
    tail_q = deque([(0, 0)])

    while True:
        time += 1
        nr = r + row[d]
        nc = c + col[d]
        if not (0 <= nr < n and 0 <= nc < n):
            return
        if grid[nr][nc] == 1:  # 내 몸이면
            return
        tail_q.append((nr, nc))
        if grid[nr][nc] == 2:
            # 사과 있으면 먹는다.
            grid[nr][nc] = 1
        else:
            # 사과 없으면
            # 땡겨야함
            tail_r, tail_c = tail_q.popleft()
            grid[tail_r][tail_c] = 0
            grid[nr][nc] = 1

        r = nr
        c = nc

        for i in range(len(rotation_list) - 1, -1, -1):
            t, direction = rotation_list[i][0], rotation_list[i][1]
            if t == time:
                rotation_list.pop(i)
                if direction == "L":
                    d = (d + 3) % 4
                else:
                    d = (d + 1) % 4
                    break
        # print("------------------")
        # for _ in grid:
        #     print(_)


game()
print(time)
