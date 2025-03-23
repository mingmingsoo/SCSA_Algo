'''
# 세번째 풀이 사다리 조건 확인하는 while문 간단히.

'''


#################################################################
# 두번째 풀이 -> 가로 연결 2개 되는 애들은 애초에 안담음
# 첫번째 풀이와 100ms 시간차이
def isOk():
    for j in range(0, m, 2):
        r, c = 0, j
        while r < n:
            # 오른쪽이나 왼쪽에 사다리 있으면 무조건 간다.
            if c > 0 and grid[r][c - 1] == 1:
                while c > 0 and grid[r][c - 1] == 1:
                    c -= 1
            elif c < m - 1 and grid[r][c + 1] == 1:
                while c < m - 1 and grid[r][c + 1] == 1:
                    c += 1
            r += 1
        if c != j:
            return False
    return True  # 여기까지 왔으면 조건 만족했음


def combi(sidx, idx, M):
    global find
    if find:
        return
    if sidx == M:
        for r, c in sel:
            grid[r][c] = 1
        if isOk():
            find = True
            return
        for r, c in sel:  # 원상복구
            grid[r][c] = 0
        return

    if idx == len(arr):
        return

    # 가로사다리 2개 연결되는지 검증
    if sidx > 0:
        pr, pc = sel[sidx - 1]  # 이전에 선택한 좌표
        r, c = arr[idx]  # 내가 선택하려는 좌표
        if pr == r and c - pc == 2:
            combi(sidx, idx + 1, M)  # 가로 2개네 ? 다음꺼 골라
            return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1, M)
    combi(sidx, idx + 1, M)


m, origin_num, n = map(int, input().split())
m = m * 2 - 1
n = n + 1
grid = [[0] * (m) for i in range(n)]

# 짝수번째가 세로 사다리, 홀수번째가 가로 사다리가 될 것임
for j in range(0, m, 2):
    for i in range(n):
        grid[i][j] = 1

# 기존 가로 사다리 남겨주기
for i in range(origin_num):
    a, b = map(lambda x: int(x) - 1, input().split())  # a가 행
    grid[a][2 * b + 1] = 1

# 0인 곳은 모두 후보가 될 수 있음.
arr = []
for i in range(n - 1):
    for j in range(m):
        if grid[i][j] == 0:
            arr.append((i, j))
row = [0, 0]
col = [-1, 1]
ans = -1
find = False
for i in range(0, 4):
    sel = [0] * i  # 후보 선택
    combi(0, 0, i)
    if find:
        ans = i
        break
print(ans)