from collections import deque

block_num = int(input())
n, m = 6, 4
green = [[0] * m for i in range(n)]
blue = [[0] * m for i in range(n)]


def location():
    if shape == 1:
        nr = n - 1
        for i in range(n):
            if green[i][c] == 1:
                nr = i - 1
                break
        green[nr][c] = 1
        nr = n - 1
        for i in range(n):
            if blue[i][3 - r] == 1:
                nr = i - 1
                break
        blue[nr][3 - r] = 1
    elif shape == 2:
        nr = n - 1
        for i in range(n):
            if green[i][c] == 1 or green[i][c + 1] == 1:
                nr = i - 1
                break
        green[nr][c] = green[nr][c + 1] = 1
        nr = n - 1
        for i in range(n):
            if blue[i][3 - r] == 1:
                nr = i - 1
                break
        blue[nr][3 - r] = blue[nr - 1][3 - r] = 1
    elif shape == 3:
        nr = n - 1
        for i in range(n):
            if green[i][c] == 1:
                nr = i - 1
                break
        green[nr][c] = green[nr - 1][c] = 1
        nr = n - 1
        for i in range(n):
            if blue[i][3 - r] == 1 or blue[i][3 - r - 1] == 1:
                nr = i - 1
                break
        blue[nr][3 - r] = blue[nr][3 - r - 1] = 1


score = 0


def delete(arr):
    global score
    while True:
        flag = False
        for i in range(n):
            if arr[i] == [1, 1, 1, 1]:
                flag = True
                arr.pop(i)
                arr.insert(0, [0, 0, 0, 0])
                score += 1
        if flag:
            # 떨어질 수 있는가 검사는 bfs,,? 미네랄 처럼 ㅠㅠ
            numbering = [[0] * m for i in range(n)]
            num = 1
            # 군집 단위로 검사하기.
            for i in range(n - 2, -1, -1):
                for j in range(m):
                    if arr[i][j] == 1 and numbering[i][j] == 0:
                        land = False
                        min_h = i
                        numbering[i][j] = num
                        q = deque([(i, j)])
                        while q:

                            r, c = q.popleft()
                            if r == n - 1:
                                land = True
                            min_h = max(min_h,r)
                            for k in range(4):
                                nr = r + row[k]
                                nc = c + col[k]
                                if not (0 <= nr < n and 0 <= nc < m) or numbering[nr][nc] != 0 or arr[nr][nc] == 0:
                                    continue
                                q.append((nr, nc))
                                numbering[nr][nc] = num
                        if not land: # 땅에 안붙어 있으면 떨군다.
                            # min_h 가 3 이면 n-minh-1 만큼 떨굴 수 있음.
                        num += 1
            print("-------------")
            for _ in numbering:
                print(_)
        else:
            break

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def special(arr):
    cnt = 0
    for i in (0, 1):
        if 1 in arr[i]:
            cnt += 1
    for count in range(cnt):
        arr.pop()
        arr.insert(0, [0, 0, 0, 0])


def total(arr):
    ele = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                ele += 1
    return ele


for b in range(block_num):
    shape, r, c = map(int, input().split())
    location()
    delete(green)
    delete(blue)
    special(green)
    special(blue)
    print("=======green=======")
    for _ in green:
        print(*_)
    print("=======blue=======")
    for _ in blue:
        print(*_)
print(score)
print(total(green) + total(blue))
