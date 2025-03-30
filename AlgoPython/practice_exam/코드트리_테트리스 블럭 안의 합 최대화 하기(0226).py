'''
# 코드트리 테트리스 블럭 안의 합 최대화 하기(백준 14500 테트로미노)

2025.03.28.금
두번째 풀이(이지만 예전에 풀어봤어서 3번째 풀이)

문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:13
    문제 종료 20:26
    총 풀이시간 13분
        13~18   : dfs 설계(5)
                    1.
                    depth가 0부터 시작이라
                        0 1 2 3
                    ex) 1 2 3 4
                    depth == 3일때 최댓값 갱신해줘야하는데 4일때 갱신해줘서 값이 크게 나와 수정!
                    2.
                    visited 어디서 처리해줘야 할지 확신이 안서서
                    일단 안쓰고 디버거 돌려서 아 여기다 해줘야겠구나 하고
                    visited 추가!
        18~22   : dfs 로 안되는 ㅜ ㅏ ㅗ ㅓ 하드코딩
        22~26   : 검증 ㅜ ㅏ ㅗ ㅓ 하나씩 테케 만들어서 검사!(4)
                    휴~ 인덱스 에러 발견! 조건 수정
                    n -> m 오타 수정

    메모리 19 KB
    시간 87 ms

문제 풀면서의 기록
dfs+하드코딩
4 5
0 0 0 0 0
0 0 0 0 0
0 0 1 1 1
0 0 0 1 0


5 4
0 0 0 0
0 0 0 0
0 0 0 1
0 0 1 1
0 0 0 1

5 4
0 0 0 0
0 0 0 0
0 0 1 0
0 0 1 1
0 0 1 0

5 4
0 0 0 0
0 0 0 0
1 0 0 0
1 1 0 1
1 0 0 0
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
ans = 0

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def dfs(r, c, sm, depth):
    global ans
    if depth == 3:
        ans = max(ans, sm)
        return
    visited[r][c] = True

    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc]:
            continue
        dfs(nr, nc, sm + grid[nr][nc], depth + 1)
    visited[r][c] = False


visited = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        dfs(i, j, grid[i][j], 0)

# ㅏ ㅓ
for i in range(n - 2):
    for j in range(m):
        sm = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
        sm1 = sm2 = sm
        if j > 0:
            sm1 += grid[i + 1][j - 1]
        if j < m - 1:
            sm2 += grid[i + 1][j + 1]
        ans = max(ans, sm1, sm2)
# ㅜ ㅗ
for i in range(n):
    for j in range(m - 2):
        sm = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        sm1 = sm2 = sm
        if i > 0:
            sm1 += grid[i - 1][j + 1]
        if i < n - 1:
            sm2 += grid[i + 1][j + 1]
        ans = max(ans, sm1, sm2)
print(ans)

'''

# 코드트리 테트리스 블럭 안의 합 최대화 하기(백준 14500 테트로미노)

문제 풀고 나서 기록

    문제 시작 15:40
    문제 종료 16:05
    총 풀이시간 25분
        0~2분    : 문제 이해 (2)
        2~3분    : 초기 주석 (1)
        3~4분    : 탑다운 구조 (1)
        4~9분    : dfs 구조 설계 (5)
        9~14분   : 답이 너무 크게나와서 디버깅 -> visited False 조건을 안넣었음
                    depth = 2면 다시 가게 하려고 했지만 디버깅 하니까 맘 처럼 잘 가지 않아서
                    하드코딩 하기로 결심, ㅏ 모양 설계 (5)
        14~21분  : ㅏ 모양 설계 완료 (7)
        22~24분  : 백준 틀려서 디버깅 (2)


    메모리 116188 KB
    시간 728 ms

    실수
    1. if not visited 를 안해서 값이 크게나와서 디버깅
    2. 백준 제출 시 디버깅하려고 남겨논 코드 안지움

    회고
    코드트리에선 맞췄는데 백준에서 틀려서 너무나 당황함.
    디버깅 하려고 찍어놨던 코드를 안지우고 제출했기 때문임
    운이 좋게도 코드트리엔 각 합이 72가 되는애가 없어서 성공한거임
    이건 평생 잘못한거라 실수코드를 안지우고 주석처리하겠음
    3주간 반성해야됨................
    테케만든거 넣어보고, 범위체크는 했으나 저 코드를 왜 보지못했을까 한탄스러움.

    ★★★★★두번 다신 이런 짓 안하겠습니다.★★★★★

    예전에 풀었던 문제라 ㅏ 모양이 난관인게 기억이나서.. 바로 캐치했지만
    처음 풀었으면 50번 틀렸을 것 같음.
    자바로 스터디했을 때 ㅏ 모양을 하드코딩 안하고 구현하는 코드를 친구가 알려줬었는데
    그게 잔상만 있고....ㅜㅜ 짜보고는 싶었으나 오히려 실수할 것 같아서 하드코딩했음.
    잔상만 있는건 잘못한거고, 실수할 것 같아서 하드코딩한건 잘한 것 같음
    역시나 dfs는 어렵다. , 하드코딩 말고 depth 조건 넣어서 다시 풀어보기

문제 설명
    모든점에서 가능한 depth가 4의 합들을 구해서 최댓값 갱신
    모양은 depth 4의 모든 경우의 수임
    그런데 ㅗ 모양이 돌아오는 로직이 필요
    -> 하드코딩 할거냐 vs 돌아올거냐
    -> 하드코딩..

필요한 메서드
    dfs

넣어본 테케(ㅜ모양이 잘 되는지)
4 6
100 100 100 1 1 1
1 100 1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1

'''


def dfs(r, c, depth, sm):
    global ans
    if depth == 4:
        ans = max(ans, sm)
        # if sm == 72:
        #     print(r,c) # 디버깅하려고 넣어놓은게 있어서 틀림 ㅠㅠ
        return

    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]

        if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc]:
            continue

        visited[nr][nc] = True
        dfs(nr, nc, depth + 1, sm + grid[nr][nc])
        visited[nr][nc] = False


n, m = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]

ans = 0

visited = [[False] * m for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, grid[i][j])  # 위치와 depth, 합
        visited[i][j] = False

# ㅏ 모양
for i in range(n - 2):
    for j in range(m - 1):
        ele_sum = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 1][j + 1]
        ans = max(ans, ele_sum)

# ㅓ 모양
for i in range(n - 2):
    for j in range(1, m):
        ele_sum = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 1][j - 1]
        ans = max(ans, ele_sum)

# ㅜ 모양
for i in range(n - 1):
    for j in range(1, m - 1):
        ele_sum = grid[i][j] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j]
        ans = max(ans, ele_sum)

# ㅗ 모양
for i in range(n - 1):
    for j in range(1, m - 1):
        ele_sum = grid[i][j] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
        ans = max(ans, ele_sum)

print(ans)
