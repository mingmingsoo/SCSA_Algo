'''
예상 풀이시간 30분
실제 풀이시간 20분

[문제설명]
    처음방향 남쪽
    좌표를 기록한다.

[구상]
    1. 임의의 점 0,0 에서 시작해서 방문한 곳을 visited(set)에 담는다. 굳이 set이 아니여도 된다.
    -> 담으면서 배열의 크기를 계산해줄 r, c 의 min, max를 구해야한다.

    2. 배열의 크기를 알아낸 뒤 #으로 채운 2차원 배열을 만든다.

    3. visited에 담긴 좌표는 이동할 수 있는 곳이므로 "."으로 바꿔준다.

'''

n = int(input())
order = input()
r, c = 0, 0  # 임의의 값: 현재 내가 서 있는 곳은 점임
visited = set([(r, c)])  # 내가 서있는 곳은 움직일 수 있는 곳

# 처음은 남쪽
d = 0
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

minR, minC, maxR, maxC = 0, 0, 0, 0
for s in order:

    # 회전한다는 것은 가려고 하는 곳에 벽이 있거나. 범위를 벗어나는 것임.
    if (s == "R"):
        d = (d + 1) % 4
    elif (s == "L"):
        d = (d - 1 + 4) % 4

    # 갈 수 있는 곳이라면.
    else:
        nr = r + row[d]
        nc = c + col[d]
        r = nr
        c = nc
        minR, minC, maxR, maxC = min(minR, r), min(minC, c), max(maxR, r), max(maxC, c)
        visited.add((r,c))

grid = [["#"] * (maxC - minC + 1) for i in range(maxR - minR + 1)]  # 배열 채우기.

for r, c in visited: # 갈 수 있는 곳 반영하기.
    r += abs(minR) # 음수값들 양수로.
    c += abs(minC)
    grid[r][c] = "."

for _ in grid:
    print("".join(_))
