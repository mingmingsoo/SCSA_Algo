'''
# 코드트리 이상한체스
2025.03.29.토
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:43
    문제 종료 21:10

    총 풀이시간 27분
        43~46   : 문제 이해 및 초기 주석(3)
        46~10   : 백트래킹 함수 설계(24)
                  오픈테케 및 1,2,3,4,5 번말 방향 잘 보는지 확인!

  메모리 17 MB
  시간 70 ms

# 문제 풀면서의 기록
말들을 모두 arr 에 담고
idx 로 모든 경우의 수를 탐색
출력은 전체 맵 크기 - 갈수 있는 체스판의 최댓값
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

arr = []
visited = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if 0 < grid[i][j] < 6:
            arr.append((i, j, grid[i][j]))
        elif grid[i][j] == 6:
            visited[i][j] = 1

ans = 0


def left(r, c, visited):
    for j in range(c, -1, -1):
        if grid[r][j] == 6:
            break
        visited[r][j] = 1

def right(r, c, visited):
    for j in range(c, m):
        if grid[r][j] == 6:
            break
        visited[r][j] = 1


def up(r, c, visited):
    for i in range(r, -1, -1):
        if grid[i][c]== 6:
            break
        visited[i][c] = 1


def down(r, c, visited):
    for i in range(r, n):
        if grid[i][c]== 6:
            break
        visited[i][c] = 1


def btk(idx):
    global ans, visited
    if idx == len(arr):
        sm = sum(map(sum, visited))
        ans = max(ans, sm)
        return

    r, c, shape = arr[idx]
    visited_copy = [_[:] for _ in visited]
    if shape == 1:
        left(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        right(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        up(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        down(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

    elif shape == 2:
        left(r, c, visited)
        right(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        up(r, c, visited)
        down(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

    elif shape == 3:
        up(r, c, visited)
        right(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        right(r, c, visited)
        down(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        down(r, c, visited)
        left(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        left(r, c, visited)
        up(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

    elif shape == 4:
        up(r, c, visited)
        right(r, c, visited)
        down(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        right(r, c, visited)
        down(r, c, visited)
        left(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        down(r, c, visited)
        left(r, c, visited)
        up(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

        left(r, c, visited)
        up(r, c, visited)
        right(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]

    elif shape == 5:
        left(r, c, visited)
        right(r, c, visited)
        up(r, c, visited)
        down(r, c, visited)
        btk(idx + 1)
        visited = [_[:] for _ in visited_copy]


btk(0)
print(n * m - ans)



'''
# 두번째 풀이
    함수화

# 문제 풀고 나서 기록

    문제 시작 13:40
    문제 종료 14:13
    총 풀이시간 33분
        40~42분  : 문제 이해(2)
        42~44분  : 문제 구상 및 초기 주석(2)
        44~01분  : cctv가 1,2 일때 로직 완료(17)
                    cctv가 1과 2만 있을 때 잘 돌아가는지 확인
                    -> 잘 돌아가서 나머지 3,4,5 cctv 로직 시작
        01~09분  : 최대한 꼼꼼히 하드코딩.(8)
                    로직완료, 테케 다 잘 돌아가는거 확인
        09~13분  : n,m 확인, 내가만든 테케로 검증, 문제 다시 읽기(4)

    메모리 115600 KB
    시간 272 ms

    회고
        1.
        생각보다 문제를 빨리 풀었는데 '내가 한번에 풀었을리가 없어..' 라고 생각하고
        테케를 만들고 검토하고 문제 재차 읽었다.

        2.
        중간에 '아 좌,우,상,하 함수를 만들자!' 생각이 들었지만
        오히려 더 실수할 것 같아서 최대한 꼼꼼하게 하드코딩했다.
        (1차 제출 이후 함수화 해서 재제출 했는데 틀림, 반증이다.
                            일단 성공하면 긴장 풀리는듯....)

문제설명
    cctv와 맵 정보가 있을 때
    사각지대를 최소로해라.
입력
    사무실 크기 N, M
    맵 정보
구상
    cctv 정보를 1차원 배열에 담고
    cctv 넘버에 따라서 완탐을 해줘야함.
    cctv 정보를 담고 idx로 넘겨서 최대 갯수 기록
테케
    4 3
    1 0 0
    0 0 0
    0 0 0
    0 0 0
    에서 1~5 모두 바꿔서 확인.

'''


def right(r, c, visited):
    ele_sm = 0
    for j in range(c + 1, m):
        if grid[r][j] == 0 and not visited[r][j]:
            ele_sm += 1
            visited[r][j] = True
        if grid[r][j] == 6:
            break
    return ele_sm


def left(r, c, visited):
    ele_sm = 0
    for j in range(c - 1, -1, -1):
        if grid[r][j] == 0 and not visited[r][j]:
            ele_sm += 1
            visited[r][j] = True
        if grid[r][j] == 6:
            break
    return ele_sm


def up(r, c, visited):
    ele_sm = 0
    for i in range(r - 1, -1, -1):
        if grid[i][c] == 0 and not visited[i][c]:
            ele_sm += 1
            visited[i][c] = True
        if grid[i][c] == 6:
            break
    return ele_sm


def down(r, c, visited):
    ele_sm = 0
    for i in range(r + 1, n):
        if grid[i][c] == 0 and not visited[i][c]:
            ele_sm += 1
            visited[i][c] = True
        if grid[i][c] == 6:
            break
    return ele_sm


def btk(idx, sm):
    global ans, visited
    if idx == len(cctv_list):
        ans = max(ans, sm)
        return

    r, c, num = cctv_list[idx]
    origin_visited = [_[:] for _ in visited]
    if num == 1:
        # 우
        btk(idx + 1, sm + right(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 왼
        btk(idx + 1, sm + left(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 위쪽을 볼 때
        btk(idx + 1, sm + up(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 밑쪽을 볼 때
        btk(idx + 1, sm + down(r, c, visited))

    elif num == 2:
        # 좌우를 볼 때
        btk(idx + 1, sm + right(r, c, visited) + left(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 상하를 볼 때
        btk(idx + 1, sm + up(r, c, visited) + down(r, c, visited))

    elif num == 3:
        # 북동
        btk(idx + 1, sm + up(r, c, visited) + right(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 동남
        btk(idx + 1, sm + down(r, c, visited) + right(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 남서
        btk(idx + 1, sm + down(r, c, visited) + left(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 서북
        btk(idx + 1, sm + up(r, c, visited) + left(r, c, visited))

    elif num == 4:
        # 위에 못볼때
        btk(idx + 1, sm + down(r, c, visited) + right(r, c, visited) + left(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 아래 못볼때
        btk(idx + 1, sm + up(r, c, visited) + right(r, c, visited) + left(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 왼쪽 못볼떄
        btk(idx + 1, sm + up(r, c, visited) + right(r, c, visited) + down(r, c, visited))
        visited = [_[:] for _ in origin_visited]

        # 오른쪽 못볼때
        btk(idx + 1, sm + up(r, c, visited) + left(r, c, visited) + down(r, c, visited))

    elif num == 5:
        btk(idx + 1, sm + up(r, c, visited) + left(r, c, visited) + down(r, c, visited) + right(r, c, visited))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

# 관리할 cctv list
cctv_list = []
for i in range(n):
    for j in range(m):
        if 0 < grid[i][j] <= 5:
            cctv_list.append((i, j, grid[i][j]))

# 내가 볼 수 있는 최대 구역 갯수
total_able_view = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            total_able_view += 1

visited = [[False] * m for i in range(n)]
ans = 0
btk(0, 0)  # cctv idx와 볼 수 있는 갯수
print(total_able_view - ans)  # 최대 - 내가 최대한 많이 본 방 갯수
