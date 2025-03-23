'''
10*10 행렬 안쓰고
'''
block_num = int(input())
green = [[0] * 4 for i in range(6)]
blue = [[0] * 4 for i in range(6)]
n = 6


def location(r, c):
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
        green[nr][c], green[nr][c + 1] = 1, 1
        nr = n - 1
        for i in range(n):
            if blue[i][3 - r] == 1:
                nr = i - 1
                break
        blue[nr][3 - r], blue[nr - 1][3 - r] = 1, 1



    elif shape == 3:
        nr = n - 1
        for i in range(n):
            if green[i][c] == 1:
                nr = i - 1
                break
        green[nr][c], green[nr - 1][c] = 1, 1
        nr = n - 1
        for i in range(n):  # 2,2
            if blue[i][3 - r] == 1 or blue[i][3 - r - 1] == 1:
                nr = i - 1
                break
        blue[nr][3 - r], blue[nr][3 - r - 1] = 1, 1


def delete(arr):
    global score
    for i in range(n):
        if arr[i].count(1) == 4:
            arr.pop(i)
            arr.insert(0, [0, 0, 0, 0])
            score += 1


def special(arr):
    cnt = 0
    for r in (0, 1):
        if 1 in arr[r]:
            cnt += 1
    for _ in range(cnt):
        arr.pop()
        arr.insert(0, [0, 0, 0, 0])


score = 0
for b in range(block_num):
    shape, r, c = map(int, input().split())
    location(r, c)
    delete(green)
    delete(blue)
    special(green)
    special(blue)

print(score)
cnt = 0
for i in range(n):
    for j in range(4):
        if green[i][j] == 1:
            cnt += 1
        if blue[i][j] == 1:
            cnt += 1
print(cnt)
